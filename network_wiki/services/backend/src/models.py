"""
Этот модуль описывающий таблицы и их поля
"""

from sqlalchemy import (
    Column,
    Integer,
    String,
)
from database import Base


class USOL2VPN(Base):
    """
    Table USOL2VPN
    """

    __tablename__ = "usol2vpn"

    id = Column(Integer, autoincrement=True, primary_key=True)
    name_uso = Column(String(100), nullable=False)
    number_uso = Column(Integer, nullable=False)
    type_uso = Column(Integer, nullable=False)
    address = Column(String(100), nullable=False)
    contact = Column(String(100), nullable=False)

    def __repr__(self):
        """
        Возвращает информацию по USO
        :return: Text
        """
        return (
            f"{self.id}, {self.name_uso}, {self.number_uso},"
            f" {self.address},"
            f" {self.contact}"
        )

    def to_json(self):
        """
        Возвращает информацию по USO
        :return: JSON
        """
        return {
            item.name_uso: getattr(self, item.name_uso)
            for item in self.__table__.columns
        }


class USOFiber(Base):
    """
    Table USOFiber
    """

    __tablename__ = "usofiber"

    id = Column(Integer, autoincrement=True, primary_key=True)
    name_uso = Column(String(100), nullable=False)
    number_uso = Column(Integer, nullable=False)
    type_uso = Column(Integer, nullable=False)
    address = Column(String(100), nullable=False)
    contact = Column(String(100), nullable=False)

    def __repr__(self):
        """
        Возвращает информацию по USO
        :return: Text
        """
        return f"{self.id}, {self.name_uso}, {self.number_uso}, {self.address}, {self.contact}"

    def to_json(self):
        """
        Возвращает информацию по USO
        :return: JSON
        """
        return {
            item.name_uso: getattr(self, item.name_uso)
            for item in self.__table__.columns
        }
