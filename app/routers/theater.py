from typing import List
from app.lib import resp
from fastapi import APIRouter
from app.models import TheaterDetails

router = APIRouter(prefix="/API/V1")


@router.post("/TheaterInfo", description="Accepts theater info.")
async def theater_detail(data: List[TheaterDetails]):

    return resp.prepare_response(data=data)
