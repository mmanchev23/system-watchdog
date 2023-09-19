from typing import List
from datetime import datetime
from pydantic import BaseModel


class HostBaseSchema(BaseModel):
    id: str | None = None
    created: datetime | None = None
    updated: datetime | None = None
    name: str

    class Config:
        orm_mode = True
        allow_population_by_field_name = True
        arbitrary_types_allowed = True


class ListHostResponse(BaseModel):
    status: str
    results: int
    hosts: List[HostBaseSchema]


class CPUDataBaseSchema(BaseModel):
    id: str | None = None
    created: datetime | None = None
    updated: datetime | None = None
    load: float
    host_id: str

    class Config:
        orm_mode = True
        allow_population_by_field_name = True
        arbitrary_types_allowed = True


class ListCPUDataResponse(BaseModel):
    status: str
    results: int
    cpu_data: List[CPUDataBaseSchema]


class RXPktBaseSchema(BaseModel):
    id: str | None = None
    created: datetime | None = None
    updated: datetime | None = None
    packets: int
    host_id: str

    class Config:
        orm_mode = True
        allow_population_by_field_name = True
        arbitrary_types_allowed = True


class ListRXPktResponse(BaseModel):
    status: str
    results: int
    rx_packets: List[RXPktBaseSchema]


class MetricsBaseSchema(BaseModel):
    time: int
    host_id: str

    class Config:
        orm_mode = True
        allow_population_by_field_name = True
        arbitrary_types_allowed = True


class MetricsResponse(BaseModel):
    status: str
    results: int
    metrics: List[MetricsBaseSchema]
