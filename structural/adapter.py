from abc import ABC, abstractmethod


# Vegetable class interface
class VegetableSalad(ABC):
    @abstractmethod
    def is_vegetable():
        pass

    @abstractmethod
    def cut_vegetable():
        pass


# Fruit class interface
class FruitSalad(ABC):
    @abstractmethod
    def is_fruit():
        pass

    @abstractmethod
    def clean_fruit():
        pass


class Vegetable(VegetableSalad):
    def __init__(self, name: str):
        self.name = name

    def is_vegetable(self):
        if isinstance(self, Vegetable):
            return f'{self.name} is vegetable'
        else:
            return f'{self.name} is not a vegetable'

    def cut_vegetable(self):
        return f'{self.name} is cut in pieces'

    def add_to_salad(self):
        return f'{self.name} is added to vegetable salad'


class Fruit(FruitSalad):
    def __init__(self, name: str):
        self.name = name

    def is_fruit(self):
        if isinstance(self, Fruit):
            return f'{self.name} is fruit'
        else:
            return f'{self.name} is not a fruit'

    def clean_fruit(self):
        return f'{self.name} is now clean'

    def eat_fruit(self):
        pass


class Adapter(Vegetable):
    def __init__(self, item: FruitSalad):
        self.item = item
        self.name = item.name

    def is_vegetable(self):
        if isinstance(self, Vegetable):
            return f'{self.item.is_fruit()} but also {self.name} is vegetable'
        else:
            return f'{self.name} is not a vegetable'


# Client works via Vegetable class interface
def client_code(vegetable: VegetableSalad):
    check_veg_is_veg = vegetable.is_vegetable()
    prepare_veg = vegetable.cut_vegetable()
    cook_veg = vegetable.add_to_salad()

    print(check_veg_is_veg)
    print(prepare_veg)
    print(cook_veg)
    print('')


if __name__ == '__main__':
    client_code(Vegetable('Tomato'))

    # Fruit class object implements Fruit class interface
    fruit = Fruit('Apple')
    adapter = Adapter(fruit)

    # Fruit class object implements Vegetable class interface via Adapter class
    check_fruit_is_veg = adapter.is_vegetable()
    prepare_fruit = adapter.cut_vegetable()
    cook_fruit = adapter.add_to_salad()

    print(check_fruit_is_veg)
    print(prepare_fruit)
    print(cook_fruit)
