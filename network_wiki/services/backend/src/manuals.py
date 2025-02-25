from fastapi import APIRouter


router = APIRouter(prefix="/manuals", tags=["manuals"])

@router.get("/manuals")
async def manuals():
    return "manuals OK", 200