"""
Builder pattern example.

Shows a ConcreteBuilder building a Product under the control of a Director.
"""

class Product:
    def __init__(self):
        self.parts = []

    def add(self, part: str):
        self.parts.append(part)

    def __str__(self):
        return f"Product parts: {', '.join(self.parts)}"


class Builder:
    def reset(self):
        raise NotImplementedError

    def produce_part_a(self):
        raise NotImplementedError

    def produce_part_b(self):
        raise NotImplementedError

    def produce_part_c(self):
        raise NotImplementedError


class ConcreteBuilder(Builder):
    def __init__(self):
        self.reset()

    def reset(self):
        self._product = Product()

    def produce_part_a(self):
        self._product.add("PartA")

    def produce_part_b(self):
        self._product.add("PartB")

    def produce_part_c(self):
        self._product.add("PartC")

    def get_result(self) -> Product:
        product = self._product
        # optionally reset to allow building a new product
        self.reset()
        return product


class Director:
    def __init__(self, builder: Builder = None):
        self._builder = builder

    def set_builder(self, builder: Builder):
        self._builder = builder

    def build_minimal_viable_product(self):
        if not self._builder:
            raise RuntimeError("Builder not set")
        self._builder.produce_part_a()

    def build_full_featured_product(self):
        if not self._builder:
            raise RuntimeError("Builder not set")
        self._builder.produce_part_a()
        self._builder.produce_part_b()
        self._builder.produce_part_c()


if __name__ == "__main__":
    builder = ConcreteBuilder()
    director = Director(builder)

    print("Standard minimal product:")
    director.build_minimal_viable_product()
    product1 = builder.get_result()
    print(product1)

    print("Standard full product:")
    director.build_full_featured_product()
    product2 = builder.get_result()
    print(product2)

    print("Custom product (client code):")
    builder.produce_part_a()
    builder.produce_part_c()
    custom = builder.get_result()
    print(custom)
