from abc import ABC, abstractmethod


# interface
class Prototype(ABC):
    @abstractmethod
    def clone():
        pass
