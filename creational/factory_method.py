from abc import ABC, abstractmethod


# interface
class Detail(ABC):
    @abstractmethod
    def create(self):
        pass

    @abstractmethod
    def to_paint(self):
        pass


# agregate class
class Auto:
    pass


class Body(Auto, ABC):
    @abstractmethod
    def create_detail() -> Detail:
        pass


class DoorCreator(Body):
    def create_detail() -> Detail:
        return Door()


class Door(Detail):
    def create(self):
        print('Door is created')

    def to_paint(self):
        print('Door is painted')


if __name__ == '__main__':
    door = DoorCreator.create_detail()
    door.create()
    door.to_paint()
