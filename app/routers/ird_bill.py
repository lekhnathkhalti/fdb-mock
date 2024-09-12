from app.lib import resp
from fastapi import APIRouter
from app.models import Bill, BillReturn

router = APIRouter(prefix="/api")


@router.post("/bill")
async def bill(data: Bill):
    return resp.prepare_response(data=data)


@router.post("/billreturn")
async def bill_return(data: BillReturn):
    return resp.prepare_response(data=data)
