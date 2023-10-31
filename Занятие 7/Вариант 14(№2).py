# -- coding: utf-8 --
import random
def srznach(array):
    print(array)
    sum = 0
    for i in range(len(array)):
        sum += i
        sr = sum / len(array)
    for i in range(len(array)):
        if array[i] > sr:
            array[i] = 1
    return array
array = [random.randint(1,10) for i in range(10)]
c = srznach(array)
print(c)
