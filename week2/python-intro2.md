# Python Intro 2

## Conditionals

Conditionals as the name suggests are used to execute code blocks depending on certain conditions.

They are mainly expressed with the if, else if (elif) and else statements.

They are based on logical conditions which have to resolve a True or False value, conditions can be chained by using logical operators such as "and", "or" and "not"

The code can be read as: if "condition is true" execute code, else if "other condition is true" execute code, else "if none of the previous conditions are true" execute code.

The example should make things a lot clearer. 

```python
# --- IF STATEMENTS----

# if, else & elif execute different code depending
# on conditions

var: str = 'String'
tmp: int = 5

if (var == 'String'):
    print('True')
else:
    print('False')

if (len(var) == 2):
    print('var is short')
elif (len(var) == 4):
    print('var is medium')
else:
    print('fml')  


if (len(var) >= 2 and len(var)<= 10):
    print('some mixed conditionals')
else:
    print('False')  

```

## What are Loops?

Loops are blocks of code that execute repeatedly (in a loop) until a condition is met. Usually this condition can be a logical statement or a range. They are a great tool to write shorter code although they should be used carefully.

Loops are often the cause of infinitely running code or particularly slow code, so a bit of care should be taken when writing them.

You should always make sure, unless you intend to run it ad infinitum, that the loop has an exit condition.

### Break and Continue

A break statement will immediately exit the current loop.

A continue statement will skip the rest of the loop and go back to the start.

### Else

An else statement at the end of a loop indicates a block of code that will always run after the loop has finished executing.



## While Loop

While loops will execute as long as a Boolean condition is not met, or a break statement is reached.

```python
# ----- LOOPS -----
# While : Execute while condition is True
END_LOOP: int = 5
w1: int = 1
while w1 < END_LOOP:
    print(w1)
    w1 += 1

END_LOOP_TWO = 20

w2: int = 0
while w2 <= END_LOOP_TWO:
    if w2 % 2 == 0:
        print(w2)
    elif w2 == 9:
        # Forces the loop to end all together
        break
    else:
        # Shorthand for i = i + 1
        w2 += 1
        # Skips to the next iteration of the loop
        continue
    w2 += 1
 
# Cycle through list
l4 = [1, 9.2, "Ule", True]
while len(l4):
    print(l4.pop(0))

END_LOOP_THREE: int = 6
i: int = 1
while i < END_LOOP_THREE:
  print(i)
  i += 1
else:
  print("i is no longer less than 6")
```

## For Loop

For loops are used to iterate over sequences. They are really useful when utilised in conjunction with collections.

```python
# For Loop
# Allows you to perform an action a set number of times
# Range performs the action 10 times 0 - 9
# end="" eliminates newline

for x in range(0, 10):
    print(x, ' ', end="")
print('\n')
 
# Cycle through list
l4 = [1, 9.2, "Ule", True]
for x in l4:
    print(x)
 
#You can also define a list of numbers to
# cycle through
for x in [2, 4, 6]:
    print(x)

# You can double up for loops to cycle through lists
numList: list[list[int]] = [[1, 2, 3], [10, 20, 30], [100, 200, 300]]

for l in numList:
    for el in l:
        print(el)
```

## Iterators

Iterators are objects that contain countable values and will return a value at the time.

```python
# ----- ITERATORS -----
# You can pass an object to iter() which returns
# an iterator which allows you to cycle thru a list
l5: list[int] = [6, 9, 12]
itr = iter(l5)
print(next(itr))  # Grab next value
 
# ----- RANGES -----
# The range() function creates integer iterables
print(list(range(0, 5)))
 
# You can define step
print(list(range(0, 10, 2)))
 
for x in range(0, 3):
    for y in range(0, 3):
        print(numList[x][y])
```
```python
# methods definitions
# methods or functions are blocks of code that are only executed when called
# all methods are defined using snake_case
# methods can take arguments (or parameters) that we "pass in" separated by a comma
# all methods are declared using the def keyword

def say_hello(name: str):
    print('hello ' + name + '!')


say_hello('Amber')
say_hello('Carlo')

def add(a: int, b: int):
    return a + b

result: int = add(5, 10)

print(result)


# talk about all the bad ideas python has when talkin' 'bout functions

# default  value

def real_slim(name = "Amber"):
  print("Hi! My name is" + name)

#declare constant instead

# variable variables key value pairs
def dog_names(dog2, dog3, dog1):
  print("Who's a good boi? you are " + dog1)

dog_names(dog1 = "Ule", dog2 = "Idaho", dog3 = "Ossi")

#this just creates confusion really

#unknown number of parameters
def horrible_children(*kids):
  print("The most horrible child is " + kids[2])

horrible_children("Emil", "Tobias", "Linus")

# just use a list or figure out what you are doing first ;)

# RECURSION

def recursion(k: int):
  if(k > 0):
    print(k)
    result = k + recursion(k - 1)
    print(f'{result}')
  else:
    result = 0
  return result


recursion(6)


# avoid tail recursion infinite loop
```

## Files

A brief tutorial on how to read in data from files. 

To setup this project we have a root directory with a files directory containing 2 files: test.txt and names.csv which are at the bottom of this tutorial.



```python
import os
#select current dir
currentDir = os.path.dirname(__file__)
currentDir = os.path.join(currentDir, 'files' )
#our file name
tFile: str = "test.txt"
#create absolute path to file
absFilePath: str = os.path.join(currentDir, tFile)
#oper file reader in read mode
f = open(absFilePath, 'r')
#print file name
print(f.mode)

#close file reader  !! very important
f.close()

#context manager automatically closes file for us
with open(absFilePath, 'r') as ff:
    # ffContents = ff.read()
    # print(ffContents)
    # select size of read in characters
    #SIZE: int = 100
    #ffContents = ff.read(SIZE)

    #read one line nad move to the next
    # ffLine = ff.readline()
    # print(ffLine)

    #read all lines
    # ffLines = ff.readlines()
    #this is a list of all the lines
    # print(ffLines)

    #read all lines using for loop
    for line in ff:
        print(line, end='')


""" csv """

import csv

#our file name
cFile: str = "names.csv"
#create absolute path to file
absFilePath: str = os.path.join(currentDir, cFile)
#open file
with open(absFilePath, 'r') as csvFile:
    csvReader = csv.reader(csvFile)
    #csv.reader(file, delimeter=";") to change delimiter

    print(csvReader)
    #just an object in memory

    #skip header  (remember iterators? :)
    next(csvReader)
    #loop to read
    for line in csvReader:
        print(line)
        # notice that line is a list already
```



### test.txt

```text
1) This is a test file
2) With multiple lines of data...
3) Third line
4) Fourth line
5) Fifth line
6) Sixth line
7) Seventh line
8) Eighth line
9) Ninth line
10) Tenth line
```

### names.csv

```text
first_name,last_name,email
John,Doe,john-doe@bogusemail.com
Mary,Smith-Robinson,maryjacobs@bogusemail.com
Dave,Smith,davesmith@bogusemail.com
Jane,Stuart,janestuart@bogusemail.com
Tom,Wright,tomwright@bogusemail.com
Steve,Robinson,steverobinson@bogusemail.com
Nicole,Jacobs,nicolejacobs@bogusemail.com
Jane,Wright,janewright@bogusemail.com
Jane,Doe,janedoe@bogusemail.com
Kurt,Wright,kurtwright@bogusemail.com
Kurt,Robinson,kurtrobinson@bogusemail.com
Jane,Jenkins,janejenkins@bogusemail.com
Neil,Robinson,neilrobinson@bogusemail.com
Tom,Patterson,tompatterson@bogusemail.com
Sam,Jenkins,samjenkins@bogusemail.com
Steve,Stuart,stevestuart@bogusemail.com
Maggie,Patterson,maggiepatterson@bogusemail.com
Maggie,Stuart,maggiestuart@bogusemail.com
Jane,Doe,janedoe@bogusemail.com
Steve,Patterson,stevepatterson@bogusemail.com
Dave,Smith,davesmith@bogusemail.com
Sam,Wilks,samwilks@bogusemail.com
Kurt,Jefferson,kurtjefferson@bogusemail.com
Sam,Stuart,samstuart@bogusemail.com
Jane,Stuart,janestuart@bogusemail.com
Dave,Davis,davedavis@bogusemail.com
Sam,Patterson,sampatterson@bogusemail.com
Tom,Jefferson,tomjefferson@bogusemail.com
Jane,Stuart,janestuart@bogusemail.com
Maggie,Jefferson,maggiejefferson@bogusemail.com
Mary,Wilks,marywilks@bogusemail.com
Neil,Patterson,neilpatterson@bogusemail.com
Corey,Davis,coreydavis@bogusemail.com
Steve,Jacobs,stevejacobs@bogusemail.com
Jane,Jenkins,janejenkins@bogusemail.com
John,Jacobs,johnjacobs@bogusemail.com
Neil,Smith,neilsmith@bogusemail.com
Corey,Wilks,coreywilks@bogusemail.com
Corey,Smith,coreysmith@bogusemail.com
Mary,Patterson,marypatterson@bogusemail.com
Jane,Stuart,janestuart@bogusemail.com
Travis,Arnold,travisarnold@bogusemail.com
John,Robinson,johnrobinson@bogusemail.com
Travis,Arnold,travisarnold@bogusemail.com
```

## User Input

With Python it is possible to get user input in a variety of ways. 

In this example we will write a little command line program to get input from a user.

We also have a little exercise at the end that should help you put together all the concepts explored in the python intro series

```python
# USER INPUT -------------
import sys 

print('What is your name?')
 
# Stores everything typed up until ENTER
name = sys.stdin.readline()
 
print('Hello', name)


# game time 

def add_two(a: int, b: int):
    return a+b

while True:
    print('first number please')
    a: int = int(sys.stdin.readline())
    print('second number please')
    b: int = int(sys.stdin.readline())
    result: int = add_two(a, b)
    print('result: '  f'{result}')
    print('press q to quit or any other key to continue')
    c: str = sys.stdin.readline().rstrip()
    if c == 'q':
        break
    else: 
        continue


# exercise time baby
#this program is fun but has many flaws
# first what if the user inputs something that is not a number?
# can you fix it?
# what if the user would like to input 3 or 4 numbers?
# can you do that?
# can you extend our little calculator to do divisions too?
# have fun
```

