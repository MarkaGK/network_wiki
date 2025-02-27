"""
Этот модуль для роутов manuals и эндпоинтов начинающихся с /manuals

"""

from fastapi import APIRouter


router = APIRouter(prefix="/manuals", tags=["manuals"])


@router.get("/manuals")
async def manuals():
    """
    Базовый эндпоинт для проверки доступности
    :return: Text
    """
    return "manuals OK", 200
