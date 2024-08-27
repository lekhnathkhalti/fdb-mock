import json

from fastapi.encoders import jsonable_encoder

from fastapi.responses import JSONResponse


def prepare_response(data: json):
    return JSONResponse(content=jsonable_encoder(data))
