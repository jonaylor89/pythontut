
'''
Section 4: List (Arrays in some languages)
==============================================
'''

''' 
Lists are boxes that hold multiple things rather than one thing
To access the things in the list you would use a for loop.
The sytax looks just the same as when you use a for loop with range
but replace range with the list.
'''
def CoolKidLists():
    # List are surrounded by brackets "[]" 
    myList = ['My', 'List', 'Elements'] # list with 3 elements
    
    print(myList[0]) # the First element is the zeroth
    print(myList[1])
    print(myList[2])
   


CoolKidLists() 
# Prints 
# My
# Lists
# Elements

'''
Lists make things really easy to manipulate a lot of numbers 
at once. Instead of going through every item manually through 
the list, programmers use something called a 'for' loop. 'for' loops
make it super easy to change every item in the list at once. 
'''

def ManipulatingAList(someList): # Notice that lists can also be inputs
    for item in someList:
        item = item + 1 # Add 1 to ever element in the list

    for element in someList: # 
        print(element)

ManipulatingAList([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) 
# Will print 
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9
# 10
# 11

'''
Adding and taking away from lists 
'''
def ElListo():
    things = [4, 5, 2, 8, 1, 8, 5, 0, 345]
    things.append(5) # To add things to a list 
    things.append(8)
    things.append(23)

    things.remove(345) # To remove things from a list
    things.remove(5)
    things.remove(23)

'''
Logic with lists
'''
def ifBilly(listOfSomeNames):
    count = 0
    for name in listOfSomeNames:
        if name == 'Billy':
            count = count + 1

    print(count)

ifBilly(['John', 'Jacob', 'Billy', 'Jingle', 'Billy', 'Schmidt', 'Billy'])
# Try to figure out what the above statement will print

'''
END Section 4: List 

Now I can write hundreds of pages about lists and all the weird things you can
do with them. There are different type of lists (list, set, array.array, queue,
tuple, etc. etc.) but the point of this section is to let you know that they
exist. To really know how useful lists are you're gonna have to write programs
yourself or watch other people (e.g. Coding Train with David Shiffman). 

Challenges
===========
1.) Write a function that takes one list input and prints every item in the list
2.) Write a function that takes one list input and multiplies 5 to every
element in the list than prints the list out. 
3.) Write a function that adds one to every element that is less than 10
