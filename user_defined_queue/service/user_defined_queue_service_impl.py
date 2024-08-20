from user_defined_queue.repository.user_defined_queue_repository_impl import UserDefinedQueueRepositoryImpl
from user_defined_queue.service.user_defined_queue_service import UserDefinedQueueService


class UserDefinedQueueServiceImpl(UserDefinedQueueService):
    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
            cls.__instance.__userDefinedQueueRepository = UserDefinedQueueRepositoryImpl.getInstance()

        return cls.__instance

    @classmethod
    def getInstance(cls):
        if cls.__instance is None:
            cls.__instance = cls()

        return cls.__instance

    def createUserDefinedQueue(self):
        self.__userDefinedQueueRepository.create()
    