from pydantic import BaseModel, EmailStr, Field
from typing import List, Optional


class USOModels(BaseModel):
    name_uso: str | None = None
    number_uso: int | None = None
    type_uso: int | None = None
    address: str | None = None
    contact: str | None = None

class USOCreate(USOModels):
    pass

class USOUpdate(USOModels):
    pass

class USOItem(USOModels):
    id: int


    class Config:
        from_attributes = True
