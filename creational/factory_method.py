from abc import ABC, abstractmethod


# interface
class Tool(ABC):
    @abstractmethod
    def draw_line(self):
        pass

    @abstractmethod
    def draw_picture(self):
        pass


# Creator abstract class
class Creator(ABC):
    @abstractmethod
    def create_tool() -> Tool:
        pass


# Concrete Creator 1
class PensilCreator(Creator):
    def create_tool(self) -> Tool:
        return Pensil()


# Concrete Creator 1 return object class
class Pensil(Tool):
    def draw_line(self):
        result = 'Pensil is drawing line'
        return result

    def draw_picture(self):
        result = 'Pensil is drawing picture'
        return result


# Concrete Creator 2
class PenCreator(Creator):
    def create_tool(self) -> Tool:
        return Pen()


# Concrete Creator 2 return object class
class Pen(Tool):
    def draw_line(self):
        result = 'Pen is drawing line'
        return result

    def draw_picture(self):
        result = 'Pen is drawing picture'
        return result


# Client Code
def client_code(creator):
    product = creator.create_tool()
    product_draw_line = product.draw_line()
    product_draw_picture = product.draw_picture()
    print(product_draw_line)
    print(product_draw_picture)


if __name__ == '__main__':
    client_code(PensilCreator())
