from app.lib import resp
from typing import List
from fastapi import APIRouter
from app.models import CancelShowDetails

router = APIRouter(prefix="/API/V1")


@router.post("/cancel_show/")
async def cancel_show(data: CancelShowDetails):
    return resp.prepare_response(data=data)
