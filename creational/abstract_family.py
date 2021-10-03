from abc import ABC, abstractmethod


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


class CastWheel(WheelFactory):
    @staticmethod
    def create_disk():
        return CastDisk()

    @staticmethod
    def create_tire():
        return CastDiskTire()

    @staticmethod
    def create_bolt():
        return CastDiskBolt()


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


class CastTire(Tire):
    def get_from_warehouse(self):
        print('Tire is now available')


class CastBolt(Bolt):
    def count_quantity(self):
        print('You need 4 bolts')
