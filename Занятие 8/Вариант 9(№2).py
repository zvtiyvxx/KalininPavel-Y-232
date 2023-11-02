# -- coding: utf-8 --
import math
import random
def massiv(array1,array2,array3):
    def procedura(array):
        sum1 = sum(array)
        srznach = sum1 / len(array)
        proizv = math.prod(array)
        return proizv, srznach
    proizv1, srznach1 = procedura(array1)
    proizv2, srznach2 = procedura(array2)
    proizv3, srznach3 = procedura(array3)
    print('Произведение 1-го массива:', proizv1)
    print('Среднее значение 1-го массива:', srznach1)
    print('Произведение 2-го массива:', proizv2)
    print('Среднее значение 2-го массива:', srznach2)
    print('Произведение 3-го массива:', proizv3)
    print('Среднее значение 3-го массива:', srznach3)
array1 = [random.randint(1,10) for i in range(10)]
array2 = [random.randint(1,10) for i in range(10)]
array3 = [random.randint(1,10) for i in range(10)]
massiv(array1,array2,array3)
