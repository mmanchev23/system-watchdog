from .database import get_db
from . import schemas, models

import psutil
import time
import uuid

from sqlalchemy.orm import Session
from fastapi import Depends, HTTPException, status, APIRouter

from sqlalchemy.exc import IntegrityError
router = APIRouter()

@router.post("/", status_code=status.HTTP_201_CREATED)
def create_metrics(payload: schemas.MetricsBaseSchema, db: Session = Depends(get_db)):
    host_id = payload.host_id
    seconds = payload.time

    host = db.query(models.Host).filter(models.Host.id == host_id).first()

    if not host:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"No host with this id: {host_id} found")

    for _ in range(seconds):
        cpu_load = psutil.cpu_percent(interval=1)
        net_stats = psutil.net_io_counters()
        rx_packets = net_stats.packets_recv

        cpu_data = models.CPUData(host_id=host_id, load=cpu_load, id=str(uuid.uuid4()))
        rxpkt = models.RXPacket(host_id=host_id, packets=rx_packets, id=str(uuid.uuid4()))

        try:
            db.add(cpu_data)
            db.add(rxpkt)
            db.commit()
            db.refresh(cpu_data)
            db.refresh(rxpkt)
        except IntegrityError:
            db.rollback() 

        time.sleep(1)

    return { "status": "success", "message": "Data was successfully retrieved!" }
