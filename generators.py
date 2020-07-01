# import sys

def eager_total(maximun):
    integers = []
    for i in range(maximun):
        integers.append(i)
    # print("Size:", sys.getsizeof(integers))
    # print(integers[:10], integers[-10:])
    # return sum(integers)
    return integers

def lazy_total(maximun):
    for i in range(maximun):
        yield i 

answer = sum(lazy_total(100))
print("Total:", answer)

