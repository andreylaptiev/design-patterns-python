# class Flyweight contains shared information about object
class Flyweight:
    def __init__(self, brand='LADA', vehicle_type='Auto'):
        self._brand = brand
        self._vehicle_type = vehicle_type

    @property
    def brand(self):
        return self._brand

    @property
    def vehicle_type(self):
        return self._vehicle_type


# class Unique contains unique information about object
class Unique:
    def __init__(self, flyweight: Flyweight, model, color):
        self._model = model
        self._color = color
        self._flyweight = flyweight

    def import_new_car(self):
        new_car = (f'Imported new {self._flyweight.vehicle_type} {self._flyweight.brand}. '
                   f'Model: {self._model}, Color: {self._color}')
        return new_car


# factory gets objects from its list or creates new
class Factory:
    available_cars = []

    def get_car(self, model, color, brand='LADA', vehicle_type='Auto'):
        car = [brand, vehicle_type, model, color]
        flyweight = Flyweight()

        if car not in self.__class__.available_cars:
            self.__class__.available_cars.append(car)
            new_car = Unique(flyweight, model, color)
            return new_car.import_new_car()

        return car


# Shop is a client and works via factory
class Shop:
    def __init__(self, factory: Factory):
        self._factory = factory

    def get_available_car(self, model, color):
        return self._factory.get_car(model, color)


# check how Flyweight class and Unique class work together
def client_code_import_car():
    flyweight = Flyweight()
    unique = Unique(flyweight, '2107', 'green')

    import_car = unique.import_new_car()
    print(import_car)


# check how factory gets available car from its list or creates a new car
def client_code_get_car():
    # Add a car to the factory list of available cars
    car = ['LADA', 'Auto', '2105', 'blue']
    Factory.available_cars.append(car)

    factory = Factory()
    shop = Shop(factory)

    # shop requests available car
    available_car = ['2105', 'blue']
    car1 = shop.get_available_car(model=available_car[0], color=available_car[1])
    print(car1)

    # shop requests unavailable car and factory creates it
    new_car = ['2101', 'white']
    car2 = shop.get_available_car(model=new_car[0], color=new_car[1])
    print(car2)


def main():
    client_code_import_car()
    client_code_get_car()


if __name__ == '__main__':
    main()
