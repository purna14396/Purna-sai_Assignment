# -*- coding: utf-8 -*-
"""Assignment_purnasai.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1flF0jZp8LidwLHAdOXB-8X6417kEvQ7A

# 1 . Working on different datatypes with examples in python 
#    (list , set , tuple , dictionary ) 


---

# **List  :**
"""

# creating a list 
fruits = ['apple', 'banana', 'orange', 'kiwi']

# accessing elements
print(fruits[0])  
print(fruits[2])

# adding elements to list
fruits.append('pear')
print(fruits)

# insert the elements at specific position 
fruits.insert(2, 'grape')
print(fruits)

# removing the elements from list
fruits.remove('kiwi')
print(fruits)

# list sclicing
print(fruits[1:3]) 
print(fruits[:2])  
print(fruits[2:])

"""# **Tuple :**"""

# creating the tuple
my_tuple = ('apple', 'banana', 'orange', 'kiwi')

# accessing the elements in tuple
print(my_tuple[0])
print(my_tuple[2])

# sclicing tuples
print(my_tuple[1:3]) 
print(my_tuple[:2])  
print(my_tuple[2:])

# coverting tuple to list
my_list = list(my_tuple)
print(my_list)

# length of the tuple
print(len(my_tuple))

"""# **Set :**"""

# creating a set
my_set = {1, 2, 3, 4, 5}

# adding elements to the set
my_set.add(6)
print(my_set) 
# adding mutiple values at a time 
my_set.update([7, 8, 9])
print(my_set)

# removing elements
my_set.remove(5)
print(my_set)

# popping a random element
print(my_set.pop())
print(my_set)

# converting the list to set
my_list = [1, 2, 3, 3, 4, 4, 5]
my_set = set(my_list)
print(my_set)

"""# **Dictionary :**"""

# creating the dictionary
my_dict = {'name': 'John', 'age': 30, 'city': 'New York'}

# accessing the elements with keys
print(my_dict['name']) 
print(my_dict['city'])

# modifying the values
my_dict['age'] = 31
print(my_dict)

# adding the new elements to dictionary
my_dict['state'] = 'NY'
print(my_dict)

# removing the elements
print(my_dict.pop('state'))
print(my_dict)

# coverting the lists to dictionary
keys = ['name', 'age', 'city']
values = ['Jane', 25, 'Los Angeles']
my_dict = dict(zip(keys, values))
print(my_dict)

"""# 2 . Working on 3 modes of files operations with examples in python
# (read ,write ,append)

---


"""

# writing into a file 
with open('a.txt', 'w') as file:
    file.write("Hii  everyone !\nI am Purna sai from sathyabama university .")
    file.close()

#  Read a file and printing the data 
with open('a.txt', 'r') as file:
    content = file.read()
    print(content)

# appending a new line to existing file "a.txt"
with open('a.txt', 'a') as file:
    file.write('\nThis is a new line. to the existing file context')
with open('a.txt', 'r') as file:
    content = file.read()
    print(content)

"""# **3 . Calculator :**"""

with open('calculator_output.txt', 'w') as file:

    num1 = float(input('Enter the first number: '))
    num2 = float(input('Enter the second number: '))
    op = input('Enter the operation (+, -, *, / , //): ')


    if op == '+':
        result = num1 + num2
    elif op == '-':
        result = num1 - num2
    elif op == '*':
        result = num1 * num2
    elif op == '/':
        result = num1 / num2
    elif op == '//':
        result = num1 // num2
    else:
        print('Invalid operator')
        result = None

    if result is not None:
        file.write(f"{num1} {op} {num2} = {result}")
        print(f"{num1} {op} {num2} = {result}")