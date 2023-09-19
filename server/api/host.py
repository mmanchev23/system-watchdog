from .database import get_db
from . import schemas, models

import uuid
from sqlalchemy.orm import Session
from fastapi import Depends, HTTPException, status, APIRouter

router = APIRouter()

# GET / -> get all hosts
@router.get("/")
def get_hosts(db: Session = Depends(get_db), limit: int = 10, page: int = 1, search: str = ""):
    skip = (page - 1) * limit
    hosts = db.query(models.Host).filter(models.Host.name.contains(search)).limit(limit).offset(skip).all()
    return { "status": "success", "results": len(hosts), "hosts": hosts }

# GET /id -> get a specific host by id
@router.get("/{host_id}")
def get_host(host_id: str, db: Session = Depends(get_db)):
    host = db.query(models.Host).filter(models.Host.id == host_id).first()

    if not host:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"No host with this id: {id} found")
    
    return { "status": "success", "host": host }

# POST / -> create a new host
@router.post("/", status_code=status.HTTP_201_CREATED)
def create_host(payload: schemas.HostBaseSchema, db: Session = Depends(get_db)):
    id = str(uuid.uuid4())
    name = payload.name
    host = models.Host(id=id, name=name)
    db.add(host)
    db.commit()
    db.refresh(host)
    return { "status": "success", "message": "Host was successfully created!", "host": host }

# PATCH /id -> update specific host
@router.patch("/{host_id}")
def update_host(host_id: str, payload: schemas.HostBaseSchema, db: Session = Depends(get_db)):
    query = db.query(models.Host).filter(models.Host.id == host_id)
    host = query.first()

    if not host:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"No host with this id: {host_id} found")
    
    update_data = payload.dict(exclude_unset=True)
    query.filter(models.Host.id == host_id).update(update_data, synchronize_session=False)
    db.commit()
    db.refresh(host)
    
    return { "status": "success", "message": "Host was successfully updated!", "host": host}

# DELETE /id -> delete specific host
@router.delete("/{host_id}")
def delete_host(host_id: str, db: Session = Depends(get_db)):
    host = db.query(models.Host).filter(models.Host.id == host_id).first()

    if not host:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"No Host with this id: {id} found")

    db.query(models.CPUData).filter(models.CPUData.host_id == host_id).delete(synchronize_session=False)
    db.query(models.RXPacket).filter(models.RXPacket.host_id == host_id).delete(synchronize_session=False)
    db.delete(host)
    db.commit()

    return {"status": "success", "message": "Host and associated data were successfully deleted!"}

