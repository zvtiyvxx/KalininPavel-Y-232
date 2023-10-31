# -- coding: utf-8 --
import random
def min_and_max_v_massive(array):
    maxindex = 0
    minindex = 0
    print(array)
    for i in range(len(array)):
        if array[i] > array[maxindex]:
            maxindex = i
        if array[i] < array[minindex]:
            minindex = i
    array[maxindex], array[minindex] = array[minindex], array[maxindex]
    return array
array = [random.randint(1,100) for i in range(10)]
c = min_and_max_v_massive(array)
print(c)
