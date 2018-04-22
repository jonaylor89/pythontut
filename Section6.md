
# Section 6: Function, input output machines
---------------------------------------------------

So far whenever I've had you write a function
I wanted the output to be printed to the screen.
This works for beginning but in normal programming
instead of printing the result of a function you would
'return' it.

Example of printing output

```python
def add2numbers(a, b):
    sumOfNums = a + b
    print(sumOfNums) # here we're printing the output to the screen

add2numbers(4, 5) # Calling the function will print 9 (simple)
```

As programs get more complex, and groups of
functions get more interconnected, you no longer
want to print output to the screen.

```python
def add2numbersPart2(a, b):
    sumOfNums = a + b
    return sumOfNums # Notice 'return' get colored  

add2numbersPart2(4, 5) # Calling the function will not print anything
```

What 'return' does is allow variables to get assigned
to function outputs. It also gives you the ability to break
out of functions early.

```python
def isBetween1and10(someNumber):
    for number in range(1, 11):
        if number == someNumber:
            return 'yes' # if the function gets to this part it is ended

    return 'no'

myVariable = isBetween1and10(6)
print(myVariable) # This should print 'yes'
```

Functions can still a prints in them but when you want
the function to stop and output something you use
'return'. I hate comparing programming to math but
it's easy to compare functions to math equations.
'y = 5x + 10', x is the input and y is equal to what is returned
by the formula.

```python
def lineFunction(x):
    m = 5
    b = 10
    y = m * x + b
    return y
```

# END Section 6: Functions, Input output machines

'return' adds a whole new layer to what functions can do.
When writing programs later, sometimes you want a function
that just prints things and other times you'll want a function
that outputs things like a math equation.

# Challenges
--------------------
1. Most of the functions we've made in previous sections use prints
where it might be better to use returns. Convert 3 challenges from previous
sections that use print and replace them with return. If you did it right
then you should be able to assign the function's output to a variable
and then print the variable. (i.e. myVar = myFunction(someInputs)
