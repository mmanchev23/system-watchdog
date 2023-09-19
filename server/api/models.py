import uuid
from sqlalchemy.sql import func
from sqlalchemy import TIMESTAMP, Column, String, Float, Integer, ForeignKey
from sqlalchemy.dialects.mysql import CHAR
from sqlalchemy.orm import relationship
from .database import Base

class Host(Base):
    __tablename__ = "hosts"

    id = Column(CHAR(36), primary_key=True, unique=True)
    created = Column(TIMESTAMP(timezone=True), nullable=False, server_default=func.now())
    updated = Column(TIMESTAMP(timezone=True), default=None, onupdate=func.now())

    name = Column(String(255), nullable=False)

class CPUData(Base):
    __tablename__ = "cpu_data"

    id = Column(CHAR(36), primary_key=True, unique=True)
    created = Column(TIMESTAMP(timezone=True), nullable=False, server_default=func.now())
    updated = Column(TIMESTAMP(timezone=True), default=None, onupdate=func.now())
    host_id = Column(CHAR(36), ForeignKey("hosts.id"))
    host = relationship("Host", backref="cpu_data")

    load = Column(Float)

class RXPacket(Base):
    __tablename__ = "rx_pkt"

    id = Column(CHAR(36), primary_key=True, unique=True)
    created = Column(TIMESTAMP(timezone=True), nullable=False, server_default=func.now())
    updated = Column(TIMESTAMP(timezone=True), default=None, onupdate=func.now())
    host_id = Column(CHAR(36), ForeignKey("hosts.id"))
    host = relationship("Host", backref="rx_pkt")

    packets = Column(Integer)
