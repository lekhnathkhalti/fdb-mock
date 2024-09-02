from app.lib import resp
from typing import List
from fastapi import APIRouter
from app.models import CancelShowDetails

router = APIRouter(prefix="/API/V1")


@router.post("/MovieInfoList")
async def movie_info(data: List[CancelShowDetails]):
    return resp.prepare_response(data=data)
