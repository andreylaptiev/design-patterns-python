from abc import ABC, abstractmethod


# interface
class Detail(ABC):
    @abstractmethod
    def create(self):
        pass

    @abstractmethod
    def to_paint(self):
        pass


# agregate class
class Auto:
    pass


class Body(Auto, ABC):
    @staticmethod
    @abstractmethod
    def create_detail():
        pass

    def install_detail(self):
        detail = self.create_detail()
        result = f'{detail.create()} and now successfully installed'
        return result


class DoorCreator(Body):
    @staticmethod
    def create_detail():
        return Door()


class Door(Detail):
    def create(self):
        result = 'Door is created'
        return result

    def to_paint(self):
        result = 'Door is painted'
        return result


def client_code(creator):
    detail = creator.create_detail()
    detail_lifeline = f'''Detail lifeline:
        {detail.create()},
        {detail.to_paint()},
        {Body.install_detail(creator)}'''
    print(detail_lifeline)


if __name__ == '__main__':
    client_code(DoorCreator)
