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
        return 'Disk is successfully painted'


class CastDiskTire(Tire):
    def get_from_warehouse(self):
        return 'Tire is now available'


class CastDiskBolt(Bolt):
    def count_quantity(self):
        return 'You need 4 bolts'


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


def client_code(factory: WheelFactory):
    disk = factory.create_disk()
    tire = factory.create_tire()
    bolt = factory.create_bolt()
    print(disk.to_paint())
    print(tire.get_from_warehouse())
    print(bolt.count_quantity())


if __name__ == '__main__':
    client_code(CastWheelFactory())
