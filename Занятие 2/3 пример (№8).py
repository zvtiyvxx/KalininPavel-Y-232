# -- coding: utf-8 --
import cmath
x = -2.235 * 10**-2
y = 2.23
z = 15.221
a = (cmath.exp(abs(x-y))) * ((abs(x-y))**(x+y))
b = cmath.atan(x) + cmath.atan(z)
c = (x**6 + cmath.log10(y)**2)**(1/3)
s = a/b + c
print(s)
