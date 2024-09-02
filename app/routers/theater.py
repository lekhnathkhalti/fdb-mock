from typing import List
from app.lib import resp
from fastapi import APIRouter
from app.models import TheaterDetails

router = APIRouter(prefix="/API/V1")


@router.post(
    "/TheaterInfo",
    description="This is an API for Theater information. This API will be hit once at the beginning of the day and if any changes is made on the API parameters like number of screen, screen capacity etc",
)
async def theater_detail(data: List[TheaterDetails]):

    return resp.prepare_response(data=data)
