import os
import sys

from fastapi import APIRouter, Depends, status
from starlette.responses import JSONResponse

from first_user_defined_function_domain.service.fudf_service_impl import FirstUserDefinedFunctionDomainServiceImpl
from user_defined_queue.repository.user_defined_queue_repository_impl import UserDefinedQueueRepositoryImpl

sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'template'))
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'template', 'include', 'socket_server'))

from template.include.socket_server.utility.color_print import ColorPrinter

firstUserDefinedFunctionDomainRouter = APIRouter()

async def injectFirstUserDefinedFunctionDomainService() -> FirstUserDefinedFunctionDomainServiceImpl:
    return FirstUserDefinedFunctionDomainServiceImpl(UserDefinedQueueRepositoryImpl.getInstance())

@firstUserDefinedFunctionDomainRouter.post("/fudf-result")
async def requestFirstUserDefinedFunctionDomainResult(firstUserDefinedFunctionDomainService: FirstUserDefinedFunctionDomainServiceImpl =
                                                      Depends(injectFirstUserDefinedFunctionDomainService)):

    firstUserDefinedFunctionDomainResult = firstUserDefinedFunctionDomainService.getResult()
    ColorPrinter.print_important_data("firstUserDefinedFunctionDomainResult", firstUserDefinedFunctionDomainResult)

    return JSONResponse(content=firstUserDefinedFunctionDomainResult, status_code=status.HTTP_200_OK)
