from sqlalchemy import (
    Column,
    Integer,
    String,
    Sequence,
    ForeignKey,
    Boolean,
    JSON,
    func,
)
from sqlalchemy.orm import relationship
from typing import Dict, Any
from database import Base


class USOL2VPN(Base):

    __tablename__ = "usol2vpn"

    id = Column(Integer, autoincrement=True, primary_key=True)
    name_uso = Column(String(100), nullable=False)
    number_uso = Column(Integer, nullable=False)
    type_uso = Column(Integer, nullable=False)
    address = Column(String(100), nullable=False)
    contact = Column(String(100), nullable=False)

    def __repr__(self):
        return f"{self.id}, {self.name_uso}, {self.number_uso}, {self.address}, {self.contact}"

    def to_json(self):
        return {
            item.name_uso: getattr(self, item.name_uso)
            for item in self.__table__.columns
        }


class USOFiber(Base):

    __tablename__ = "usofiber"

    id = Column(Integer, autoincrement=True, primary_key=True)
    name_uso = Column(String(100), nullable=False)
    number_uso = Column(Integer, nullable=False)
    type_uso = Column(Integer, nullable=False)
    address = Column(String(100), nullable=False)
    contact = Column(String(100), nullable=False)

    def __repr__(self):
        return f"{self.id}, {self.name_uso}, {self.number_uso}, {self.address}, {self.contact}"

    def to_json(self):
        return {
            item.name_uso: getattr(self, item.name_uso)
            for item in self.__table__.columns
        }
