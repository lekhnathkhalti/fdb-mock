from app.lib import resp
from typing import List
from fastapi import APIRouter, Request
from app.models import TheaterData

router = APIRouter(prefix="/API/V1")


@router.post("/cancel_show/")
async def cancel_show(data: List[TheaterData]):
    return resp.prepare_response(data=data)
