from abc import ABC, abstractmethod


class BuildingInterface(ABC):
    @abstractmethod
    def build_mall(self):
        pass


class BuildingService(BuildingInterface):
    def build_mall(self):
        return 'The mall is built'


class BuildingProxy(BuildingInterface):
    def __init__(self, building):
        self._building = building

    @staticmethod
    def count_cost():
        return 'Building mall costs 1 mln usd'

    def is_profitable(self):
        if not self.count_cost():
            return 'Building is profitable'

        return f'{self.count_cost()}. Building is not profitable'

    def build_mall(self):
        profit = self.is_profitable()

        if not profit:
            return f'{profit}\n{self._building.build_mall()}'

        return f'{profit}\nBuilding denied.'


def client_code(building: BuildingInterface):
    mall = building.build_mall()
    return mall


def main():
    # Build mall straight via building service
    building_service = BuildingService()
    mall1 = client_code(building_service)
    print(mall1)
    print('')

    # Build mall via building proxy after counting its cost and checking is it profitable
    building_proxy = BuildingProxy(building_service)
    mall2 = client_code(building_proxy)
    print(mall2)


if __name__ == '__main__':
    main()
