from typing import List
from app.lib import resp
from fastapi import APIRouter
from app.models import TheaterData

router = APIRouter(prefix="/API/V1")


@router.post("/theater/", description="This is my description")
async def theater_detail(data: List[TheaterData]):

    return resp.prepare_response(data=data)
