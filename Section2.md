
# Section 2: Logic
-------------------------

So far our functions have been boring
e.g.

```python
def printStuff(a, b, c, d):
    print(a)
    print(b)
    print(c)
    print(d)
```

The way programmers make function do cool things is with logic
i.e. (true, false)

This function takes in two numbers and prints the bigger one

```python
def max_value(number1, number2):
    if number1 < number2: # !!! This line is where the logic is
        print(number2)
    else:
        print(number1)
```

If you've ever been in a math class than the '<'
sign should be familiar. The above function
checked if number2 was greater than number1.
If it was true than it runs the code under the if (i.e. print(number2))
If it wasn't true it would run the code under the else (i.e. print(number1))

```python
max_value(1, 10) # Calling this function prints 10
max_value(4, 3) # Here it prints 4
```

More examples to try and help it make sense:

```python
def are_they_equal(a, b):
    if a == b: # Here is the logic in this function.
        print('yes')
    else:
        print('no')

def equal_to_or_less_than(gradeInClass, GradeNeededToPass):
    if gradeInClass <= GradeNeededToPass:
        print('You failed')
    else:
        print('You good for now')

are_they_equal('John', 'John') # Should print yes
equal_to_or_less_than(45, 80) # prints You failed

```

1. '<' and '>' are pretty easy
2. '<=' and '>=' less than or equal to and great than or equal to
3. '==' and '!=' means equal to and not equal to (In CS '!' means not)

Those are the 'logical operators' in programming



# END of Section 2: Logic

Logic and logical operators become vital in later sections
This section may have seemed simple but it's important
you completely understand what's happening. We're only at the beginning.

# Challenges
----------------------

1. Write a function that takes one input and prints it if it equals 42
2. Write a function that takes two arguments and prints 'no' if they aren't equal and 'yes' otherwise.
