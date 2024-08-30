from fastapi import Header, HTTPException


async def check_custom_headers(
    Username: str = Header(None),
    Password: str = Header(None),
    TheaderCode: str = Header(None),
):
    if not all([Username, Password, TheaderCode]):
        HTTPException(status_code=401, detail="Required header parameters are missing.")
