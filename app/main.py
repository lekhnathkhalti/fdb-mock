from fastapi import FastAPI, Depends
from app.lib.header_checker import check_custom_headers
from app.middlewares.headercheckr import HeaderValidationMiddleware
from app.routers import theater, ticket, return_ticket, show, cancel_show

app = FastAPI()

app.add_middleware(HeaderValidationMiddleware)

app.include_router(
    theater.router, tags=["Theater"], dependencies=[Depends(check_custom_headers)]
)
app.include_router(
    ticket.router, tags=["Ticket"], dependencies=[Depends(check_custom_headers)]
)
app.include_router(
    return_ticket.router,
    tags=["Ticket Return"],
    dependencies=[Depends(check_custom_headers)],
)
app.include_router(
    show.router, tags=["Show"], dependencies=[Depends(check_custom_headers)]
)
app.include_router(
    cancel_show.router,
    tags=["Ticket Cancel"],
    dependencies=[Depends(check_custom_headers)],
)
