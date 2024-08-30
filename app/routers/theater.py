from typing import List
from app.lib import resp
from fastapi import APIRouter
from app.models import TheaterDetails

router = APIRouter(prefix="/API/V1")


@router.post("/theater", description="This is my description")
async def theater_detail(data: TheaterDetails):

    return resp.prepare_response(data=data)
