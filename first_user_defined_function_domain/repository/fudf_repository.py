from abc import ABC, abstractmethod


class FirstUserDefinedFunctionDomainRepository(ABC):
    @abstractmethod
    def getResult(self, userDefinedReceiverFastAPIChannel):
        pass
