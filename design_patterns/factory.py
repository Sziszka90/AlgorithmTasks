"""
Factory pattern example.
"""

from abc import ABC, abstractmethod


class Product(ABC):
    @abstractmethod
    def do(self):
        pass


class ConcreteA(Product):
    def do(self):
        return "A"


class ConcreteB(Product):
    def do(self):
        return "B"


class Factory:
    @staticmethod
    def create(kind: str) -> Product:
        if kind == 'A':
            return ConcreteA()
        elif kind == 'B':
            return ConcreteB()
        raise ValueError('Unknown kind')


if __name__ == "__main__":
    a = Factory.create('A')
    b = Factory.create('B')
    print(a.do(), b.do())
