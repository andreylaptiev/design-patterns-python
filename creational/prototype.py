import copy


class Auto:
    def __init__(self, wheels_quantity, engine):
        self.wheels_quantity = wheels_quantity
        self.engine = engine

    def __copy__(self):
        new = self.__class__(self.wheels_quantity, self.engine)
        new.__dict__.update(self.__dict__)
        return new


if __name__ == '__main__':
    auto = Auto(4, True)
    auto_copy = copy.copy(auto)
    print(auto_copy)
