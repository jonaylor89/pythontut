

# Section 5: Loops, doing the same thing a million times
---------------------------------------------------------

When programming, a lot of the time you're gonna
want to do something a bunch of times. For example
if you wanted to print the numbers 1 - 100 on the screen.
The solution to this is to make a loop. The most common
loop is a 'for' loop which is in the next function.

```python
def printingNums():
    for x in range(1, 101): # The beautiful for loop
        print(x)

printingNums() # I already said this would print 1 through 100
```

The syntax of for loops looks a lot like English
making it pretty easy to understand. For every 'x'
in range 1, 101 ('range' going to 1 less than the limit
you give it) print x

```python
def negatives(integer):
    for number in range(-integer, integer+1):
        print(number)

negatives(5) # prints -5 to 5
```

Any number can be put into 'range' positive or negative as long as it doesn't have a decimal
e.g. range(1.4, 5.4) doesn't work. You'll get an error.

```python
def yourNumber(myNumber):
    for num in range(1, 11):
        if num == myNumber: # Oh yes, logic and loops. A vicious combination
            print('Your number is between 1 and 10')

yourNumber(2) # prints myNumber is between 1 and 10
yourNumber(15) # prints nothing
```

There is another kind of loop called a 'while' loop.
While loops go while a certain logical condition is true
(e.g. while some_number > 10: )

Most situations won't require a while loop which is why for loops
are much more popular. The main use of while loops now would be to
purposely make an infinite loop (A loop that never stops). (while True:)
Infinite loops get used a loop in network programming.

```python
def goForever(startingNumber):
    while True:
        print(startingNumber)
        startingNumber = startingNumber + 1

# goForever(5) <= if you run this you will print numbers out forever
# (Or until you cancel your program)
```

# END of Section 5: loops

Loops are another one of those things that
are super useful but can also get fucking crazy.
In later sections I'm going to show you some crazier
things for loops can do.

# Challenges
--------------------

1. Write a function that prints the numbers 10 - 42
2. Write a function that loops through 1 - 100 and prints the numbers greater
than 55 out
3. Write a function that prints 'Yo Dawg' 4 times
