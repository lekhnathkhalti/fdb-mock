from fastapi import FastAPI

from app.routers import theater, ticket, return_ticket, show, cancel_show

app = FastAPI()

app.include_router(theater.router, tags=["Theater"])
app.include_router(ticket.router, tags=["Ticket"])
app.include_router(return_ticket.router, tags=["Ticket Return"])
app.include_router(show.router, tags=["Show"])
app.include_router(cancel_show.router, tags=["Ticket Cancel"])
