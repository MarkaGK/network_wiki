"""
Этот модуль предназначен для валидации данных
"""

# pylint: disable=too-few-public-methods

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
    """
    Класс валидации при добавлении нового USO
    """


class USOUpdate(USOModels):
    """
    Класс валидации при обновлении USO
    """


class USOItem(USOModels):
    """
    Класс валидации при поиске USO по id
    """

    id: int

    class Config:
        """
        Класс для подтягивания орм модели
        """

        orm_mode = True
