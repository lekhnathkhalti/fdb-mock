from app.lib import resp
from typing import List
from fastapi import APIRouter
from app.models import TicketReturnDetails

router = APIRouter(prefix="/API/V1")


@router.post("/return_ticket")
async def return_ticket(data: List[TicketReturnDetails]):
    return resp.prepare_response(data=data)
