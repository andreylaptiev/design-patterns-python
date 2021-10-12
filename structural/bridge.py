from abc import ABC, abstractmethod


# implementation class, interface
class DrinkMaker(ABC):
    @abstractmethod
    def set_bottle_material():
        pass

    @abstractmethod
    def set_taste():
        pass


# cocrete drink maker 1
class WaterMaker(DrinkMaker):
    def __init__(self, taste='No taste', bottle_material='Plastic'):
        self.taste = taste
        self.bottle_material = bottle_material

    def set_bottle_material(self):
        return f'Water bottle material is {self.bottle_material}'

    def set_taste(self):
        return f'Water taste is {self.taste}'


# cocrete drink maker 2
class JuiceMaker(DrinkMaker):
    def __init__(self, taste, bottle_material='Paper'):
        self.taste = taste
        self.bottle_material = bottle_material

    def set_bottle_material(self):
        return f'Juice bottle material is {self.bottle_material}'

    def set_taste(self):
        return f'Juice taste is {self.taste}'


# abstraction class
class Drink:
    def __init__(self, maker: DrinkMaker):
        self.maker = maker

    def make_drink(self):
        return f'{self.maker.set_bottle_material()}. {self.maker.set_taste()}'


# special type of drink
class SpecialGlassedJuice(Drink):
    def __init__(self, *args):
        super().__init__(*args)

    def make_drink(self):
        special_drink = f'''Special glassed juice.\
            {self.maker.set_bottle_material()}.\
            {self.maker.set_taste()}'''.replace('  ', '')
        return special_drink


# client code works only via abstraction class
def client_code(drink: Drink):
    requested_drink = drink.make_drink()
    print(requested_drink)


def main():
    water_maker = WaterMaker()
    juice_maker = JuiceMaker('Orange')

    water = Drink(water_maker)
    juice = Drink(juice_maker)

    client_code(water)
    client_code(juice)
    print('#')

    special_juice_maker = JuiceMaker('Special orange', 'Glass')

    special_juice = SpecialGlassedJuice(special_juice_maker)

    client_code(special_juice)


if __name__ == '__main__':
    main()
