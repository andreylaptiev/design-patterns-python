from abc import ABC, abstractmethod


# interface
class Detail(ABC):
    @abstractmethod
    def create(self):
        pass

    @abstractmethod
    def to_paint(self):
        pass


class Auto(ABC):
    @abstractmethod
    def create_detail(self) -> Detail:
        pass


class Body(Auto):
    @staticmethod
    def create_detail() -> Detail:
        return Door()


class Door(Detail):
    def create(self):
        print('Door is created')

    def to_paint(self):
        print('Door is painted')


if __name__ == '__main__':
    door = Body.create_detail()
    door.create()
    door.to_paint()
    # print(type(door))
    print(isinstance(door, Door))
    print(type(door))
    print(door)
