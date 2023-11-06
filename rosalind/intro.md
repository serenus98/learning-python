# INI1 - Installing Python

I installed Python 3.11 according to the instructions on the python.org website.

# INI2 - Variables and Some Arithmetic

```python
a = int(input("a = ", ))
b = int(input("b = ", ))
c = a**2 + b**2
print("c =", round(c))
```
# INI3 - Strings and Lists

```python
text = input("Input the String: ")
index1 = input("Input the first index: ")
index2 = input("Input the second index: ")
index3 = input("Input the third index: ")
index4 = input("Input the fourth index: ")


print(text[int(index1):int(index2)+1], text[int(index3):int(index4)+1])
