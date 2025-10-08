"""
Observer pattern example.
"""

class Subject:
    def __init__(self):
        self._observers = []

    def attach(self, obs):
        self._observers.append(obs)

    def detach(self, obs):
        self._observers.remove(obs)

    def notify(self, msg):
        for o in self._observers:
            o.update(msg)


class Observer:
    def __init__(self, name):
        self.name = name

    def update(self, msg):
        print(f"{self.name} received: {msg}")


if __name__ == "__main__":
    s = Subject()
    o1 = Observer('o1')
    o2 = Observer('o2')
    s.attach(o1)
    s.attach(o2)
    s.notify('hello')
    s.detach(o1)
    s.notify('world')
