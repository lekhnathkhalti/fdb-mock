from app.lib import resp
from typing import List
from fastapi import APIRouter
from app.models import TicketDetails

router = APIRouter(prefix="/API/V1")


@router.post("/ticket/")
async def ticket(data: List[TicketDetails]):
    return resp.prepare_response(data=data)
