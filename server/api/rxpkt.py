from .database import get_db
from . import schemas, models

import uuid
from sqlalchemy.orm import Session
from fastapi import Depends, HTTPException, status, APIRouter

router = APIRouter()

@router.get("/{host_id}")
def get_rxpkt(host_id: str, db: Session = Depends(get_db), limit: int = 10, page: int = 1):
    skip = (page - 1) * limit
    rxpkt = db.query(models.RXPacket).filter(models.RXPacket.host_id == host_id).limit(limit).offset(skip).all()
    count = db.query(models.RXPacket).filter(models.RXPacket.host_id == host_id).count()

    if not rxpkt:
        return { "status": "error", "message": "No Packets found!" }

    return { "status": "success", "count": count, "page": page, "rxpkt": rxpkt }

@router.post("/", status_code=status.HTTP_201_CREATED)
def create_rxpkt(payload: schemas.RXPktBaseSchema, db: Session = Depends(get_db)):
    host_id = payload.host_id

    host = db.query(models.Host).filter(models.Host.id == host_id).first()

    if not host:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No host found!")

    id = str(uuid.uuid4())
    packets = payload.packets

    rxpkt = models.RXPacket(id=id, host_id=host_id, packets=packets)
    db.add(rxpkt)
    db.commit()
    db.refresh(rxpkt)
    return { "status": "success", "rxpkt": rxpkt }
