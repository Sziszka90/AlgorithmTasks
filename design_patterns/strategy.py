"""
Strategy pattern example.
"""

from abc import ABC, abstractmethod


class Strategy(ABC):
    @abstractmethod
    def execute(self, data):
        pass


class ConcreteStrategyA(Strategy):
    def execute(self, data):
        return [x * 2 for x in data]


class ConcreteStrategyB(Strategy):
    def execute(self, data):
        return [x + 1 for x in data]


class Context:
    def __init__(self, strategy: Strategy):
        self.strategy = strategy

    def run(self, data):
        return self.strategy.execute(data)


if __name__ == "__main__":
    ctx = Context(ConcreteStrategyA())
    print(ctx.run([1, 2, 3]))
    ctx.strategy = ConcreteStrategyB()
    print(ctx.run([1, 2, 3]))
