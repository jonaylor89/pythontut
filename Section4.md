
# Section 4: List (Arrays in some languages)
------------------------------------------

Lists are boxes that hold multiple things rather than one thing.
They are huge variables that generally hold values that are related to each other
but technically they don't have to be.

```python
def CoolKidLists():
    # List are surrounded by brackets "[]"
    myList = ['My', 'List', 'Elements'] # list with 3 elements

    print(myList[0]) # the First element is the zeroth index
    print(myList[1])
    print(myList[2])

CoolKidLists()
# Prints:
# My
# Lists
# Elements
```

Lists can hold any data type (i.e. integers (1, 2, 3, etc.), floating point numbers (1.123, 2.45, 12.67, etc.), characters (a, b, c, etc.)) They are also order which means [1, 2, 3] is different from [3, 2, 1].

Adding and taking away things from lists

```python
def ElListo():
    things = [4, 5, 2, 8, 1, 8, 5, 0, 345]
    things.append(5) # To add things to a list
    things.append(8)
    things.append(23)

    things.remove(345) # To remove things from a list
    things.remove(5)
    things.remove(23)

```

Logic with lists

```python
def ifBilly(listOfSomeNames):
    count = 0
    for name in listOfSomeNames:
        if name == 'Billy':
            count = count + 1

    print(count)

ifBilly(['John', 'Jacob', 'Billy', 'Jingle', 'Billy', 'Schmidt', 'Billy'])
# Try to figure out what the above statement will print
```

# END Section 4: List

Now I can write hundreds of pages about lists and all the weird things you can
do with them. There are different type of lists (list, set, array.array, queue,
tuple, etc. etc.) but the point of this section is to let you know that they
exist. To really know how useful lists are you're gonna have to write programs
yourself or watch other people (e.g. Coding Train with David Shiffman).

# Challenges
---------------------------
1. Write a function that takes one list input and prints the first element in the lists
2. Write a function that takes two list inputs and prints the product of their first elements
