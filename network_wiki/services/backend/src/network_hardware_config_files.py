from fastapi import APIRouter


router = APIRouter(prefix="/confiles", tags=["confiles"])

@router.get("/confiles")
async def get_network_hardware_config_files():
    return "network_hardware_config_files OK"
