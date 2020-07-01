# import sys

def eager_total(maximun):
    numbers = []
    for i in range(maximun):
        numbers.append(i)
    # print("Size:", sys.getsizeof(numbers))
    # print(numbers[:10], numbers[-10:])
    # return sum(numbers)
    return numbers

def lazy_total(maximun):
    for i in range(maximun):
        yield i 

answer = sum(lazy_total(100))
print("Total:", answer)

