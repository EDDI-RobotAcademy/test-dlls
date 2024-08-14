from abc import ABC, abstractmethod


class UserDefinedQueueService(ABC):
    @abstractmethod
    def createUserDefinedQueue(self):
        pass
