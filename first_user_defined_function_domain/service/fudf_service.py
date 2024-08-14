from abc import ABC, abstractmethod


class FirstUserDefinedFunctionDomainService(ABC):
    @abstractmethod
    def getResult(self):
        pass
    