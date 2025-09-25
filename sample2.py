import random


def getRandomXY():
    x1 = random.randint(1, 100)
    y1 = random.randint(1, 100)
    return x1, y1


# retrieving return values individually.
# note the difference in the print output and how it inserts variable values
x,y = getRandomXY()
print(f"x is {x} and y is {y}")
print("x is of type {} and y is of type {}".format(type(x), type(y)))


# Note that when you have multiple return values, you can capture them individually as shown above, or you can capture them as a tuple as shown here:

listVal = getRandomXY()
print(listVal)
print(f"x is {listVal[0]} and y is {listVal[1]}. y is a type { type(listVal)} variable")

# this code throws an error because it receives 2 values but wants to receive 3
x,y,z = getRandomXY()
print(x)