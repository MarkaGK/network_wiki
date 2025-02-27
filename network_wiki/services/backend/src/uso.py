"""
Этот модуль для роутов uso и эндпоинтов начинающихся с /uso
"""

from fastapi import APIRouter
from sqlalchemy import select, update, delete
from models import USOFiber, USOL2VPN
from database import async_session_maker
from schemas import USOUpdate, USOCreate
router = APIRouter(prefix="/uso", tags=["uso"])

@router.get("/uso")
async def get_network_hardware_config_files():
    """
    Базовый эндпоинт для проверки доступности
    :return: Text
    """
    return "USO OK"

@router.get("/l2vpn", status_code=201)
async def get_uso_fiber():
    """
    Эндпоинт который возвращает список всех USO из таблицы L2VPN
    :return: list
    """
    async with async_session_maker() as session:
        result = await session.execute(select(USOL2VPN))
        all_uso = result.scalars().all()
        return all_uso

@router.post("/l2vpn")
async def add_uso_l2vpn(model: USOCreate):
    """
    Эндпоинт который добавляет новый USO в таблицу L2VPN
    :param model: USOCreate
    :return: Text
    """
    async with async_session_maker() as session:
        async with session.begin():
            new_uso = USOL2VPN(
                name_uso=model.name_uso,
                number_uso=model.number_uso,
                type_uso=model.type_uso,
                address=model.address,
                contact=model.contact
            )
            session.add(new_uso)
            await session.commit()
    return "New Uso added", 201


@router.put("/l2vpn/{uso_id}")
async def update_uso_l2vpn(uso_id: int, item: USOUpdate):
    """
    Эндпоинт который обновляет запрашиваемый USO из таблицы L2VPN по id
    :param uso_id: int
    :param item: USOUpdate
    :return: Text
    """
    async with async_session_maker() as session:
        async with session.begin():
            cur_uso_id = await session.execute(select(USOL2VPN.id))
            if uso_id not in cur_uso_id.scalars().all():
                return "USO not found", 404

            stmt = (
                update(USOL2VPN)
                .where(USOL2VPN.id == uso_id)
                .values(
                    name_uso=item.name_uso,
                    number_uso=item.number_uso,
                    type_uso=item.type_uso,
                    address=item.address,
                    contact=item.contact
                )
            )
            await session.execute(stmt)
            await session.commit()

    return "Uso updated", 201


@router.delete("/l2vpn/{uso_id}")
async def delete_uso_l2vpn(uso_id: int):
    """
    Эндпоинт который удаляет запрашиваемый USO из таблицы L2VPN по id
    :param uso_id: int
    :return: Text
    """
    async with async_session_maker() as session:
        async with session.begin():
            cur_uso_id = await session.execute(select(USOL2VPN.id))
            if uso_id not in cur_uso_id.scalars().all():
                return "USO not found", 404

            stmt = (
                delete(USOL2VPN)
                .where(USOL2VPN.id == uso_id)
            )
            await session.execute(stmt)
            await session.commit()

    return "Uso deleted", 201


@router.get("/fiber", status_code=201)
async def get_uso_fiber():
    """
    Эндпоинт который возвращает список всех USO в таблице USOFiber
    :return: list
    """
    async with async_session_maker() as session:
        result = await session.execute(select(USOFiber))
        all_uso = result.scalars().all()
        return all_uso


@router.post("/fiber")
async def add_uso_fiber(model: USOCreate):
    """
    Эндпоинт который добавляет новый USO в таблицу USOFiber по id
    :param model: USOCreate
    :return: Text
    """
    async with async_session_maker() as session:
        async with session.begin():
            new_uso = USOFiber(
                name_uso=model.name_uso,
                number_uso=model.number_uso,
                type_uso=model.type_uso,
                address=model.address,
                contact=model.contact
            )
            session.add(new_uso)
            await session.commit()
    return "New Uso added", 201


@router.delete("/fiber/{uso_id}")
async def delete_uso_fiber(uso_id: int):
    """
    Эндпоинт который удаляет USO из таблицы USOFiber по id
    :param uso_id: int
    :return: Text
    """
    async with async_session_maker() as session:
        async with session.begin():
            cur_uso_id = await session.execute(select(USOL2VPN.id))
            if uso_id not in cur_uso_id.scalars().all():
                return "USO not found", 404

            stmt = (
                delete(USOL2VPN)
                .where(USOL2VPN.id == uso_id)
            )
            await session.execute(stmt)
            await session.commit()

    return "Uso deleted", 201

