from app.lib import resp
from typing import List
from fastapi import APIRouter
from app.models import MovieInfo

router = APIRouter(prefix="/API/V1")


@router.post("/MovieInfoList")
async def movie_info(data: List[MovieInfo]):
    return resp.prepare_response(data=data)
