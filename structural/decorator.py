from abc import ABC, abstractmethod


class HumanClothes(ABC):
    @abstractmethod
    def wear_clothes(self):
        pass


class DefaultHumanClothes(HumanClothes):
    def __init__(self, default_human_clothes='underwear and socks'):
        self._default_human_clothes = default_human_clothes

    def wear_clothes(self):
        result = f'Default human clothes: {self._default_human_clothes}'
        return result


class BaseDecorator(HumanClothes):
    def __init__(self, default_clothes: HumanClothes):
        self._default_clothes = default_clothes

    @property
    def default_clothes(self):
        return self._default_clothes

    def wear_clothes(self):
        return self._default_clothes.wear_clothes()


class InsideClothesDecorator(BaseDecorator):
    def wear_clothes(self):
        inside_clothes = 'Inside clothes: t-shirt and trousers'
        return f'{self.default_clothes.wear_clothes()}\n{inside_clothes}'


class OutsideClothesDecorator(BaseDecorator):
    def wear_clothes(self):
        outside_clothes = 'Outside clothes: jacket and boots'
        return f'{self.default_clothes.wear_clothes()}\n{outside_clothes}'


def client_code_base(default_human_clothes: HumanClothes):
    base_decorator = BaseDecorator(default_human_clothes)
    print(base_decorator.wear_clothes())


def client_code_inside(default_human_clothes: HumanClothes):
    inside_clothes_decorator = InsideClothesDecorator(default_human_clothes)
    print(inside_clothes_decorator.wear_clothes())


def client_code_outside(default_human_clothes: HumanClothes):
    inside_human_clothes = InsideClothesDecorator(default_human_clothes)
    outside_clothes_decorator = OutsideClothesDecorator(inside_human_clothes)
    print(outside_clothes_decorator.wear_clothes())


def main():
    default_human_clothes = DefaultHumanClothes()
    client_code_base(default_human_clothes)

    print('#\nInside clothes:\n')
    client_code_inside(default_human_clothes)

    print('#\nOutside clothes:\n')
    client_code_outside(default_human_clothes)


if __name__ == '__main__':
    main()
