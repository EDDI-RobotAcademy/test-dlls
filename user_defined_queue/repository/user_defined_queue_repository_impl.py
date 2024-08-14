import multiprocessing

from user_defined_queue.repository.user_defined_queue_repository import UserDefinedQueueRepository


class UserDefinedQueueRepositoryImpl(UserDefinedQueueRepository):
    __instance = None

    __systemSocketReceiverFastAPIChannel = None
    __systemFastAPISocketTransmitterChannel = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)

        return cls.__instance

    @classmethod
    def getInstance(cls):
        if cls.__instance is None:
            cls.__instance = cls()

        return cls.__instance

    def getUserDefinedSocketReceiverFastAPIChannel(self):
        return self.__systemSocketReceiverFastAPIChannel

    def getUserDefinedFastAPISocketTransmitterChannel(self):
        return self.__systemFastAPISocketTransmitterChannel

    def create(self):
        self.__systemSocketReceiverFastAPIChannel = multiprocessing.Queue()
        self.__systemFastAPISocketTransmitterChannel = multiprocessing.Queue()
    