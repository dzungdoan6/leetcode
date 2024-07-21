from queue import Queue
class MovingAverage:

    def __init__(self, size: int):
        self.q = Queue(maxsize=size)
        for i in range(size):
            self.q.put(0)
        
        self.sum = 0
        self.counter = 0
        self.size = size

    def next(self, val: int) -> float:
        self.counter = self.counter + 1 if self.counter < self.size else self.counter
        rmv = self.q.get()
        self.q.put(val)
        self.sum = self.sum - rmv + val
        return self.sum / self.counter

# test case 1
movingAverage = MovingAverage(3)
print(movingAverage.next(1))
print(movingAverage.next(10))
print(movingAverage.next(3))
print(movingAverage.next(5))

# test case 2
movingAverage = MovingAverage(1)
print(movingAverage.next(-1))
