from abc import ABC, abstractmethod


# interface
class Detail(ABC):
    def create(self):
        pass

    def to_paint(self):
        pass

    def install(self):
        pass


class Auto(ABC):
    @abstractmethod
    def create_detail(self):
        pass
