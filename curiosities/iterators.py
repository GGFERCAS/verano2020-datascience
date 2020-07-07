import time

class Powers:
    def __init__(self, exponent):
        self.exponent = exponent

    def __iter__(self):
        self.base = 0
        return self

    def __next__(self):
        if self.base == 100:
            raise StopIteration
        self.base += 1
        return self.base ** self.exponent


squares = Powers(2)


for n in squares:
    print(n)
    time.sleep(0.1)