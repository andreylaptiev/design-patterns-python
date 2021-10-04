from abc import ABC, abstractmethod


class Disk(ABC):
    @abstractmethod
    def to_paint(self):
        pass

    def check_quality(self):
        return True


class Tire(ABC):
    @abstractmethod
    def get_from_warehouse(self):
        pass

    def check_state(self):
        return True


class Bolt(ABC):
    @abstractmethod
    def count_quantity(self):
        pass

    def check_strength(self):
        return True


class CastDisk(Disk):
    def to_paint(self):
        print('Successfully painted')


class CastDiskTire(Tire):
    def get_from_warehouse(self):
        print('Tire is now available')


class CastDiskBolt(Bolt):
    def count_quantity(self):
        print('You need 4 bolts')


# interface
class WheelFactory(ABC):
    @abstractmethod
    def create_disk():
        pass

    @abstractmethod
    def create_tire():
        pass

    @abstractmethod
    def create_bolt():
        pass


class CastWheelFactory(WheelFactory):
    @staticmethod
    def create_disk():
        return CastDisk()

    @staticmethod
    def create_tire():
        return CastDiskTire()

    @staticmethod
    def create_bolt():
        return CastDiskBolt()


class Application:
    pass
    # def create_wheel(self):
    #     pass

    # def to_balane_wheel():
    #     pass


def client_code(factory):
    disk = factory.create_disk()
    tire = factory.create_tire()
    bolt = factory.create_bolt()
    print(disk.check_quality())


if __name__ == '__main__':
    client_code(CastWheelFactory())
