#from math import *
a = int(input("a = "))
b = int(input("b = "))
result = 0
if a % 2 == 0:
    for num in range(a+1, b+1, 2):
        result += num
else:
    for num in range(a, b+1, 2):
        result += num
        #print(num)
print(result)