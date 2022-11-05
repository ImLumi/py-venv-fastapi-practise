from pydantic import BaseModel
from typing import Optional


class CreateMessurePlaceData(BaseModel):
    place: str
    messure_type: str
    messure_record: Optional[list] = []
