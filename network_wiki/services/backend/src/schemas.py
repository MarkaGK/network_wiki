"""
Этот модуль предназначен для валидации данных
"""


from pydantic import BaseModel


class USOModels(BaseModel):
    """
    Модель необходимых данных для добавления в таблицы
    """
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
        orm_mode = True
