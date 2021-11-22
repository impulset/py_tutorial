from typing import Dict, List, Set, Optional
from pydantic import BaseModel, validator
from pydantic.errors import cls_kwargs
from pydantic.types import Json
from sqlalchemy.sql.sqltypes import Boolean
from datetime import date

class All_work_orders(BaseModel):
    order_id: int
    start_date: str
    start_time:str
    type: str
    hours: int
    rate: int
    location: str
    title: str
    day: str
    class Config:
        orm_mode = True    
    
    @validator('type')
    def static_mage(cls, type):
        return f'/static/{type}'
