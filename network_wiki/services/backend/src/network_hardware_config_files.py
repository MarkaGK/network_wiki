"""
Этот модуль для роутов confiles и эндпоинтов начинающихся с /confiles
"""

from fastapi import APIRouter


router = APIRouter(prefix="/confiles", tags=["confiles"])

@router.get("/confiles")
async def get_network_hardware_config_files():
    """
    Базовый эндпоинт для проверки доступности
    :return: Text
    """
    return "network_hardware_config_files OK"
