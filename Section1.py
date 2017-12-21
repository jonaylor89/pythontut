''' 
Author: John Naylor

Tutorial for teaching basic programming using python
Words following a '#' character are called comments
They are used to document sections of code
They do NOT affect what the program does

It is super inportant that you follow along and write
the code I have written. It will build muscle
memory and help things make sense more. The only way to learn 
how to program is to write programs.

Through this page I will have simple coding challenges
for you to do. If you can't do the challenges at the section
you're at then you need to reread the section. 

'''

'''
Section 1: Functions, the building blocks of programming
===========================================================
'''

'''
 A function is a container code
 Most programs written in the real world are just
 Collections of function arranged in a particular manner
 Like building blocks
 
 This function just prints out Hello World when 'called'
'''
def FirstFunction():
    print("Hello World")


FirstFunction() # This line is 'calling'(CS term for running a function) the function 

'''
 Function can also be given inputs
 This function will get two numbers as inputs
 After adding the numbers together it prints the sum
'''
def add2numbers(a, b):
    NumberSum = a + b
    print(NumberSum)

'''
 Since this function takes inputs (a, b) 
 When calling it, you must tell the function
 what a and b are like so
'''
add2numbers(5, 6) # In this case I'm making a=5 and b=6
add2numbers(10, 35) # I can use whatever numbers I want


'''
 Notice that I can name functions whatever I want
 (Although it's nice to name function easy to remember things

 Also notice that I can name the inputs whatever I want
 (In add2numbers it's a and b but in multiplyNumbers it's num1 and num2
'''
def multiplyNumbers(num1, num2):
    product = num1 * num2 
    print(product)


'''
END of Section 1
=====================

This section is meant to just introduce you to the basic of functions
Function are super fucking cool and can do crazy things but for now
You just need to now that they will hold blocks of code 
(The next section will show you what I mean by 'code')

Challenges!
============
1.) Write a function that takes one inputs and prints that number
(Don't overthink this, It should be super fucking easy)

2.) Write a function that takes two inputs and prints their difference
(subtraction)

3.) Write a function that take two inputs and prints them quotient
(Division)
'''
