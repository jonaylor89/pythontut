
##### Author: John Naylor

Through this page I will have simple coding challenges
for you to do. If you can't do the challenges at the section
you're at then you need to reread the section.

# Section 1: Functions, the building blocks of programming
--------------------------------------------------------------

A function is a container of code
Most programs written in the real world are just
collections of function arranged in a particular manner
like building blocks

This function just prints out Hello World when 'called'

```python
def FirstFunction():
    print("Hello World")
```

And executing the function looks like...

```python
FirstFunction()
```

Functions can also be given inputs.
This function will get two numbers as inputs
after adding the numbers together it prints the sum

```python
def add2numbers(a, b):
    NumberSum = a + b
    print(NumberSum)
```

Since this function takes two input 'a' and 'b',
when calling it, you must tell the function
what a and b are like so

```python
add2numbers(5, 6) # In this case I'm making a=5 and b=6
add2numbers(10, 35) # I can use whatever numbers I want
```


Notice that I can name functions whatever I want
(Although it's nice to name function easy to remember things)

Also notice that I can name the inputs whatever I want
(In add2numbers it's a and b but in multiplyNumbers it's num1 and num2

```python
def multiplyNumbers(num1, num2):
  product = num1 * num2
  print(product)
```


# END of Section 1
-------------------------

This section is meant to just introduce you to the basic of functions
Function are super cool and can do crazy things but for now
You just need to know that they will hold blocks of code
(The next section will show you what I mean by 'code')

# Challenges!
------------------------
1. Write a function that takes one inputs and prints that number
(Don't overthink this, It should be super fucking easy)

2. Write a function that takes two inputs and prints their difference
(subtraction)

3. Write a function that take two inputs and prints them quotient
(Division)



Solutions:
    - Please go back up and attempt the challenge honstly.
    - If you still have trouble go to the tutorial

1.
```python
def function_(num):
    print(num)
```

2. 

```python
def diff_(num1, num2):
    diff_ = num1 - num2
    print(diff_)
```

3.

```python
def div_(num1, num2):
    div_ = num1/num2
    print(div_)
```