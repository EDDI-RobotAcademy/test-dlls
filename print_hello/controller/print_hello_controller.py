from fastapi import APIRouter, Depends, status
from starlette.responses import JSONResponse

printHelloRouter = APIRouter()


@printHelloRouter.get("/print-hello")
async def requestPrintHello():
    return JSONResponse(content="Hello DLLS~~!!~!", status_code=status.HTTP_200_OK)
