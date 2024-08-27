from app.lib import resp
from typing import List
from fastapi import APIRouter
from app.models import ReturnTicketDetails

router = APIRouter(prefix="/API/V1")


@router.post("/return_ticket/")
async def return_ticket(data: List[ReturnTicketDetails]):
    return resp.prepare_response(data=data)
