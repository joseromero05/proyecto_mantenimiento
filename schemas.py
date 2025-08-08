from pydantic import BaseModel
from datetime import datetime

class RequestCreate(BaseModel):
    user_id: int
    equipment_id: int
    type: str
    description: str

class RequestOut(BaseModel):
    id: int
    user_id: int
    equipment_id: int
    type: str
    description: str
    status: str
    created_at: datetime

    class Config:
        orm_mode = True
