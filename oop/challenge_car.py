class Car:
    def __init__(self, max_veloc):
        self.max_veloc = max_veloc
        self.actual_veloc = 0

    def accelerate(self, delta=5):
        _max = self.max_veloc
        new = self.actual_veloc + delta
        self.actual_veloc = new if new <= _max else _max
        return self.actual_veloc

    def _break(self, delta=5):
        new = self.actual_veloc - delta
        self.actual_veloc = new if new >= 0 else 0
        return self.actual_veloc
        

if __name__ == '__main__':
    c1 = Car(180)

    for _ in range(25):
        print(c1.accelerate(8))

    for _ in range(10):
        print(c1._break(delta=20))
