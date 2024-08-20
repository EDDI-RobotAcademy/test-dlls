import os
import sys

from first_user_defined_function_domain.repository.fudf_repository_impl import FirstUserDefinedFunctionDomainRepositoryImpl
from first_user_defined_function_domain.service.fudf_service import FirstUserDefinedFunctionDomainService
from user_defined_queue.repository.user_defined_queue_repository_impl import UserDefinedQueueRepositoryImpl

sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'template'))
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'template', 'include', 'socket_server'))

from template.include.socket_server.utility.color_print import ColorPrinter


class FirstUserDefinedFunctionDomainServiceImpl(FirstUserDefinedFunctionDomainService):
    def __init__(self, userDefinedQueueRepository: UserDefinedQueueRepositoryImpl):
        self.__firstUserDefinedFunctionDomainRepository = FirstUserDefinedFunctionDomainRepositoryImpl()
        self.__userDefinedQueueRepository = userDefinedQueueRepository

    def getResult(self):
        userDefinedReceiverFastAPIChannel = self.__userDefinedQueueRepository.getUserDefinedSocketReceiverFastAPIChannel()
        ColorPrinter.print_important_data("userDefinedReceiverFastAPIChannel", userDefinedReceiverFastAPIChannel)
        return self.__firstUserDefinedFunctionDomainRepository.getResult(userDefinedReceiverFastAPIChannel)


