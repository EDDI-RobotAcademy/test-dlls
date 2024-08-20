from abc import ABC, abstractmethod


class UserDefinedQueueRepository(ABC):
    @abstractmethod
    def create(self):
        pass
