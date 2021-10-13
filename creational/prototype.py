from abc import ABC, abstractmethod
import copy


# abstract class
class Prototype(ABC):
    registry = []

    @classmethod
    def get_prototype(cls):
        prototype_object = Prototype.registry[0]
        new_object = prototype_object
        new_object.__dict__.update(prototype_object.__dict__)
        return new_object

    def reg_prototype(self):
        Prototype.registry.append(
            self.__class__(self.auto_type, self.wheels_quantity)
            )
        return None

    @abstractmethod
    def clone():
        pass


class Auto(Prototype):
    def __init__(self, auto_type, wheels_quantity):
        self.auto_type = auto_type
        self.wheels_quantity = wheels_quantity

    def __copy__(self):
        new_object = self.__class__(self.auto_type, self.wheels_quantity)
        new_object.__dict__.update(self.__dict__)
        return new_object

    def clone(self):
        clone = copy.copy(self)
        return clone


if __name__ == '__main__':
    auto = Auto('Bus', 4)
    auto.reg_prototype()

    # get new object from prototype registry
    prototype = Prototype.get_prototype()
    print(prototype)
    print(prototype.auto_type)

    # get new object from clone method
    clone = auto.clone()
    print(clone)
    print(clone.auto_type)
