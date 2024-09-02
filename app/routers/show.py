from app.lib import resp
from typing import List
from fastapi import APIRouter
from app.models import ShowDetails

router = APIRouter(prefix="/API/V1")


@router.post("/show")
async def show(data: List[ShowDetails]):
    return resp.prepare_response(data=data)
