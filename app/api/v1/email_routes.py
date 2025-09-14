from fastapi import APIRouter

router = APIRouter()

@router.get("/fetch")
async def fetch_emails():
    return {"status": "emails fetched"}
