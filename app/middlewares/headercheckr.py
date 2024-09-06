from fastapi import Request, HTTPException
from starlette.middleware.base import BaseHTTPMiddleware


class HeaderValidationMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        header_fields = ["Username", "Password", "TheaterCode"]

        if not all([f in request.headers for f in header_fields]):
            raise HTTPException(
                status_code=401, detail="Required parameters cannot be empty"
            )

        response = await call_next(request)

        return response
