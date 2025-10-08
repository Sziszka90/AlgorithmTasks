"""
Singleton pattern example.

This file shows a simple thread-unsafe singleton using __new__.
"""

class Singleton:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance._init(*args, **kwargs)
        return cls._instance

    def _init(self, value=None):
        self.value = value


if __name__ == "__main__":
    s1 = Singleton(10)
    s2 = Singleton(20)
    print("s1.value", s1.value)
    print("s2.value", s2.value)
    print("s1 is s2:", s1 is s2)
