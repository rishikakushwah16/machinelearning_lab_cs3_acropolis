# -*- coding: utf-8 -*-
"""Copy of 3 Lists.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1angw-Acj7ooqcCDdHEThQhtaZI8UDHMB

# Lists
"""



"""## Lists
- A list is a collection of items, that is stored in a variable. 
- The items should be related in some way, but there are no restrictions on what can be stored in a list.

### Syntax
list-name = [list of comma seperated values]

### Slicing with list

index start with 0

 listname[index_number]

 listname[start_index:end_index]

 listname[:end_index]

 listname[start_index:]


negative index: 
 listname[:-index] 


### list methods
- append()
- len()
- insert(index,value)
- sort()
- reverse()
- pop(), pop(index)
- min(), max(), sum()


We can change the contents of the lists after its creation

listname[index]=newvalue

#### Task 1: Run below code and try to make some changes to the code
"""

# list creation
countries = ['India', 'Australia', 'USA']

# print whole list
print(countries)

# Accessing list elements
print("Value at 0 index: ",countries[0])

# assignning new value to index
countries[0]='Japan'

print("New value at index 0: ",countries[0])

countries=['INDIA','USA','AUSTRALIA','NEW ZEALAND']
print(countries)
print("Value at 0 index:",countries[0])
countries[0]='china'
print("new value at index 0",countries[0])



"""### Iterating lists

#### Task 2: Run below code and try to make some changes to the code
"""

hybridlists=['My name is',
             'I am in',
             3,
             'Semester']

print(hybridlists)

# we can access the elements of list using loops

for item in hybridlists:
    print(item)

hybridlists=['my name is',
             'i am in',
             6,
             'semester',
             3,
             'year'
             ]
print(hybridlists)
for item in hybridlists:
  print(item)

"""#### Task 3: Run below code and try to make some changes to the code"""

# print the index number with value

countries = ['India', 'Australia', 'USA']

for index, country in enumerate(countries):
    place = str(index)
    print("Index: " + place + ", Value: " + country.title())
    
# find index of
index = countries.index('India') 
print("\n Index of India is: ",index)

countries=['INDIA','USA','UAE','UK','AUSTRALIA']
for index, country in enumerate(countries):
  place=str(index)
  print("INDEX:"+place+",value:"+country.title())
  index=countries.index('UAE')
  print("\n INDEX OF INDIA IS ",index)

"""#### Task 4: Run below code and try to make some changes to the code"""

# Remove the last country from the list by index or by value
del countries[2]

print(countries)

del countries[3]
print(countries)

"""### List comprehension (with for loop)

#### Task 5: Run below code and try to make some changes to the code
"""

# without comprehension

cubes = []
for x in [1, 2, 3, 4, 5]:
    cubes.append(x ** 3) 
    
print(cubes)

squares=[]
for x in [1,2,3,4,5,6]:
  squares.append(x**2)
print(squares)

# with comprehension
  
cubes= [x**3 for x in [1, 2, 3, 4, 5]]
print(cubes)

squares=[x**2 for x in [1,2,3,4,5,6]]
print(squares)

numbers=[1,2,3,4,5,6,7,8,9,10]
list=[x for x in numbers]
list

"""#### Program 1: Write a python program which does the following
- Make a list that includes four job types , such as 'programmer', 'truck driver' and so on
- Use the *list.index()* function to find the index of one job type in your list.
- Use the *in* function to show that this job type is in your list.
- Use the *append()* function to add a new job type to your list.
- Use the *insert()* function to add a new job type "Python Programmer" at the beginning of the list.
- Use a loop to show all the job types in your list.
"""

# start writing your code after this line
jobs=['programmer','truck driver','analyst','doctor','teacher']
for index,i in enumerate(jobs):
  p=str(index)
  print("INDEX:"+p+" , value: "+i.title())
for j in jobs:
  jobs.append('artist')
  jobs.insert(0,'python programmer')
print(jobs)

"""#### Problem 2: Write a python program for following

- Make a list that includes the names of five famous people.
- Remove each person from the list, one at a time, using the four methods given below:
    - Del item from the list by del: del listname[index]
    - Remove the item from the list by remove method: listname.remove('itemname')
    - Using pop() method, It removes the last item from the list: listname.pop() 
    - Pop any item from the list by index: listname: listname.pop(index)
- Print out a message that there are no famous people left in your list, and print your list to prove that it is empty.
"""

# start writing your code after this line
name=['lincoln','gandhi','martin luther king','teresa','mark twain']
del name[2]
print(name)
name.remove('teresa')
print(name)
name.pop()
print(name)
name.pop(1)
print(name)

"""#### Program 3: Write a python program which does the following

- Store the first ten letters of the alphabet in a list.
- Use a slice to print out the first three letters of the alphabet.
- Use a slice to print out any three letters from the middle of your list.
- Use a slice to print out the letters from any point in the middle of your list, to the end.
"""

# Making the alphabet list
Alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']

# Printing out First 3 letters
print(Alphabet[:3])

# Printing out any 3 letters from middle
print(Alphabet[3:6])

# Printing out last 5 elements
print(Alphabet[5:])

"""#### Program 4: Write a python program for following

- Your goal in this exercise is to prove that copying a list protects the original list.
- Make a list with three people's names in it.
- Use a slice to make a copy of the entire list.
- Add at least two new names to the new copy of the list.
- Make a loop that prints out all of the names in the original list, along with a message that this is the original list.
- Make a loop that prints out all of the names in the copied list, along with a message that this is the copied list.
"""

People_Orig = ['sita', 'gita', 'meera']

# Making a Copy
People_Copy = People_Orig[:]

# Adding 2 People
People_Copy.append('MONEY')
People_Copy.append('nira')

# Displaying Original List
print("This is the Original List...")
for name in People_Orig:
  print(name)

print()
# Displaying Copied List
print("This is the copied List...")
for name in People_Copy:
  print(name)

"""#### Program 5: Write a python program for following

- Create a list to store the marks of top 15 students obtained by the students in Python Quiz held on 21/08/2018. Maximum marks=15
- Print the maximum marks obtained by the student from the list.
- Print the minimum marks obtained by the student.
- Find the sum of all the marks.
- Find the average of the marks.
- Reverse the original list and display using for loop.
"""

Marks = [11, 14, 15, 10, 11, 10, 13, 14, 13, 12, 15, 11, 12, 13, 15]

print("Maximum marks obtained: ", max(Marks))
print("Minimum marks obtained: ", min(Marks))
print("Sum of marks obtained: ", sum(Marks))
print("Average marks obtained: ", sum(Marks)/15)

rev_marks = Marks[::-1]
print("Reversed list is: ", rev_marks)

"""#### Program 6: Write a program in Python to create a list which contains n integers entered by the user and delete all odd numbers from the list. Example: If initial contents of the list is=[1,2,3,4,5,6,7,8,9,10], the output would be=[2,4,6,8,10]."""

# write your code after this line
n = int(input("Enter any number: "))
Numbers = []

for i in range(n):
  Num = int(input("Enter the number: "))
  Numbers.append(Num)

print("Initial List: ", Numbers)

for i in Numbers:
  if i%2 != 0:
    Numbers.remove(i)

print("Updated List: ", Numbers)

"""## Optional Questions

#### Program 7: Write a python program for following.
- Create an initial empty list named "countries" 
- Read the names of n countries from the user and add them to country list:
- Use for loop to display all the names of the countries from the list and add "is Great" after the country name if it is "India"
"""

# write code after this line

"""### Program 8: Write a Python program to find the list in a list of lists whose sum of elements is the highest.
Sample lists: [[1,2,3], [4,5,6], [10,11,12], [7,8,9]]
Expected Output: [10, 11, 12]
"""



