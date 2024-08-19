from abc import ABC, abstractmethod

class UserDefinedQueueRepository(ABC):
    @abstractmethod
    def getUserDefinedSocketReceiverFastAPIChannel(self):
        pass

    @abstractmethod
    def getUserDefinedFastAPISocketTransmitterChannel(self):
        pass

    @abstractmethod
    def create(self):
        pass
