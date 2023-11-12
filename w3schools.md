# if ... else

## Exercises

```Pyhton
#Exercise 1
a = 50
b = 10
if a > b:
  print("Hello World")
#a is greater than b so the code prints "Hello World"
#Exercise 2
#Print "Hello World" if a is not equal to b.
a = 50
b = 10
if a != b:
  print("Hello World")
#Exercise 3
#Print "Yes" if a is equal to b, otherwise print "No".
a = 50
b = 10
if a == b:
  print("Yes")
else:
  print("No")
#Exercise 4
#Print "1" if a is equal to b, print "2" if a is greater than b, otherwise print "3".
a = 50
b = 10
if a == b:
  print("1")
elif a > b:
  print("2")
else:
  print("3")
#Exercise 5
#Print "Hello" if a is equal to b, and c is equal to d.
if a == b and c == d:
  print("Hello")
#Exercise 6
#Print "Hello" if a is equal to b, or if c is equal to d.
if a == b or c == d:
  print("Hello")
#Exercise 7
#This example misses indentations to be correct.
#Insert the missing indentation to make the code correct:
if 5 > 2:
    print("Five is greater than two!")
#Exercise 8
#Use the correct short hand syntax to put the following statement on one line:
if 5 > 2: print("Five is greater than two!")
#Exercise 9
#Use the correct short hand syntax to write the following conditional expression in one line:
print("Yes") if 5 > 2  else print("No")
```


# for loop

The *else:* block in a for loop is not executed after a break statement.

## Exercise

```Pyhton
#Exercise 1
#Loop through the items in the fruits list.
fruits = ["apple", "banana", "cherry"]
for x in fruits
  print(x)
#Exercise 2
#In the loop, when the item value is "banana", jump directly to the next item.
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    continue
  print(x)
#Exercise 3
#Use the range function to loop through a code set 6 times.
for x in range(6):
  print(x)
#Exercise 4
#Exit the loop when x is "banana".
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    break
  print(x)
```
# boolean
```Python
#Exercise 1
#The statement below would print a Boolean value, which one?
print(10 > 9)
True
#Exercise 2
#The statement below would print a Boolean value, which one?
print(10 == 9)
False
#Exercise 3
#The statement below would print a Boolean value, which one?
print(10 < 9)
False
#Exercise 4
#The statement below would print a Boolean value, which one?
print(bool("abc"))
True
#Exercise 5
#The statement below would print a Boolean value, which one?
print(bool(0))
False
```
