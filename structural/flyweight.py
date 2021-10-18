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

    @property
    def model(self):
        return self._model

    @property
    def color(self):
        return self._color

    def import_new_car(self):
        new_car = (f'Imported new {self._flyweight.vehicle_type} {self._flyweight.brand}. '
                   f'Model: {self._model}, Color: {self._color}')
        return new_car


# factory creates new objects
class Factory:
    available_models = []

    # def __init__(self, flyweight: Flyweight, unique: Unique):
    #     self._car_info = [flyweight.brand, flyweight.vehicle_type, unique.model, unique.color]
    #     self.__class__.available_models.append(self._car_info)

    @classmethod
    def get_model(cls, brand='LADA', vehicle_type='Auto', model=None, color=None):
        model = [brand, vehicle_type, model, color]
        flyweight = Flyweight()

        if model not in cls.available_models:
            cls.available_models.append(model)
            return Unique(flyweight, model, color)

        return model


# Shop is a client
class Shop:
    def __init__(self, factory: Factory):
        self._factory = factory

    def get_available_car(self, car_info):
        return self._factory.get_model(car_info)


# check new car import
def client_code_import_car():
    flyweight = Flyweight()
    unique = Unique(flyweight, '2107', 'green')

    import_car = unique.import_new_car()
    print(import_car)


# check how factory gets available car and creates new car
def client_code_get_car():
    # Add new available car to factory list
    available_car = ['LADA', 'Auto', '2107', 'green']
    Factory.available_models.append(available_car)

    factory = Factory()
    shop = Shop(factory)

    # get a car from available and create new
    get_available_car = ['LADA', 'Auto', '2107', 'green']
    create_new_car = ['Volga', 'Auto', '24', 'green']

    shop.get_available_car(get_available_car)
    shop.get_available_car(create_new_car)


def main():
    client_code_import_car()
    client_code_get_car()


if __name__ == '__main__':
    main()
