from fastapi import APIRouter

router = APIRouter()

@router.get("/ping")
async def ping_calendar():
    return {"status": "calendar module works"}
