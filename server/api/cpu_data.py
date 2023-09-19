from .database import get_db
from . import schemas, models

import uuid
from sqlalchemy.orm import Session
from fastapi import Depends, HTTPException, status, APIRouter

router = APIRouter()

@router.get("/{host_id}")
def get_cpu_data(host_id: str, db: Session = Depends(get_db), limit: int = 10, page: int = 1):
    skip = (page - 1) * limit
    cpu_data = db.query(models.CPUData).filter(models.CPUData.host_id == host_id).limit(limit).offset(skip).all()
    count = db.query(models.CPUData).filter(models.CPUData.host_id == host_id).count()

    if not cpu_data:
        return { "status": "error", "message": "No CPU data found!" }

    return { "status": "success", "count": count, "page": page, "cpu_data": cpu_data }

@router.post("/", status_code=status.HTTP_201_CREATED)
def create_cpu_data(payload: schemas.CPUDataBaseSchema, db: Session = Depends(get_db)):
    host_id = payload.host_id
    host = db.query(models.Host).filter(models.Host.id == host_id).first()

    if not host:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No host found!")

    id = str(uuid.uuid4())
    load = payload.load

    cpu_data = models.CPUData(id=id, host_id=host_id, load=load)
    db.add(cpu_data)
    db.commit()
    db.refresh(cpu_data)
    return { "status": "success", "cpu_data": cpu_data }
