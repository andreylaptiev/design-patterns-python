from abc import ABC, abstractmethod


class Builder(ABC):
    @property
    @abstractmethod
    def product(self):
        pass

    @abstractmethod
    def set_box(self):
        pass

    @abstractmethod
    def set_electronics(self):
        pass

    @abstractmethod
    def set_drive(self):
        pass


class VideoPlayer:
    def __init__(self):
        self.configuration = {}

    def add_box(self, box_type):
        self.configuration.update({'Box type': box_type})

    def add_electronics(self, electronics_type):
        self.configuration.update({'Electronics': electronics_type})

    def add_drive(self, drive_type):
        self.configuration.update({'Drive': drive_type})

    def check_configuration(self):
        return self.configuration


class VideoPlayerBuilder(Builder):
    def __init__(self):
        self.reset()

    def reset(self):
        self._product = VideoPlayer()

    # get product
    @property
    def product(self):
        product = self._product
        self.reset()
        return product

    def set_box(self):
        self._product.add_box('Black box')

    def set_electronics(self):
        self._product.add_electronics('Video electronics')

    def set_drive(self):
        self._product.add_drive('DVD')


class Director:
    def __init__(self):
        self._builder = None

    @property
    def builder(self):
        return self._builder

    @builder.setter
    def builder(self, builder):
        self._builder = builder

    def build_videoplayer(self):
        self.builder.set_box()
        self.builder.set_electronics()
        self.builder.set_drive()


def client_code():
    director = Director()
    builder = VideoPlayerBuilder()
    director.builder = builder
    director.build_videoplayer()
    configuration = builder.product.check_configuration()
    print(f'Player configuration: {configuration}')


if __name__ == '__main__':
    client_code()
