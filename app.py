import math, random  # we have to import "math module" if we want math methods;
from utils import find_max, kg_to_lbs  # methods of importing modules;
from pathlib import Path
import sys
import os
from pprint import pprint

# print("max number", find_max([1, 20, 5]))
# print("kilogram to pounds", kg_to_lbs(20))

# "None" in python is something like "null" in JavaScript

# -----------------------------------------------------------------

# sys.exit()

### Variables and their methods:
name = "ismoil"
surname = "sharifov"
multi_lines = "     I'm Sharifov Ismoil.\tA Full-Stack Developer, who loves coding.\n\nNow I'm learning new progamming-language\python"
cleaned = multi_lines.strip()
title = "menu".upper()
# print(title.center(20, "="))
# print("Coffee".ljust(16, ".") + "$2".rjust(4))
# print("Muffin".ljust(16, ".") + "$5".rjust(4))
# print("Cheesecake".ljust(16, ".") + "$8".rjust(4))
# print("")
# print("Ismoil".startswith("I"))
# print("Ismoil".endswith("s"))

# FORMATTED STRING: - it is something similar to backticks in JavaScript;
text1 = "%s has %s best friends" % ("Ismoil", "over 10")
# print(text1)
text2 = "{} has {} best friends".format("Ismoil", "over 10")
# print(text2)
text3 = f"{name} {surname} is a programmer and he is {12.5 * 2:.2f}"
# print(text3)

# -----------------------------------------------------------------
course = "Python Course for Beginners"
exists = "for" in course
doesnt_exists = "JavaScript" in course
# print(exists, doesnt_exists)
# -----------------------------------------------------------------
x = 50 / 3  # this one gives an answer without rounding;
b = 50 // 3  # this one rounds float to integer;
# print(x, b)
# -----------------------------------------------------------------

### IF ELSE CONDITIONS:
# weight = input("Your Weight? ")
# unit = input("is it in 'Kg' or 'Lb'? ")

# if unit.lower() == "kg":
#   converted = int(weight)*2.2
#   print(f"your weight is = {converted} pounds")
# elif unit.lower() == "lb":
#   converted = int(weight)//2.2
#   print(f"your weight is = {converted} kg")

# -----------------------------------------------------------------

### LOOPS:
# guesses = 0
# secret_num = 5

## While Loop:
# while guesses < 3:
#   guess = int(input("Guess Number! "))
#   guesses += 1
#   if guess == secret_num:
#     print("You WON!!!")
#     break
# else: # we can use "else condition", but if the loop breaks then the condition doesn't work;
#   print("Sorry, You FAILED")

## For Loop:
# for i in range(2, 22, 2):
#   print(i)
# else: print("the end of the loop")


# -----------------------------------------------------------------

### LISTS - it is like what is called "array" in JS:
nums = [1, 2, 23, 230, 3, 231, 4, 5, 10, 23, 50, 44, -50]

### There is 2D-Lists in Python that represent Math Metrix:
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
]

### Lists Methods:
matrix[0][0] = 20  # modifying an item;
matrix.append(10)  # adding to the end of the list;
matrix.insert(1, 12)  # adding to a specific index;
matrix.remove([20, 2, 3])  # removing a specific list item
matrix.pop()  # it removes the last item of the list;
matrix.clear()  # clearing the entire list
# del matrix[1:2] # deleting the entire list or some of its values
nums.index(230)  # it returns the index of the first occurance;
existance = (
    50 in nums or 50 not in nums
)  # this is one is safer since it returns boolean value;
nums.count(23)  # this one returns the total occurances of a passed value;
nums.sort()  # this one sorts but does not return a new list;
nums.reverse()  # reversing the sorted order;
nums.append(26)

# copying list:
nums2 = (
    nums.copy()
)  # this method is better choice of copying a list then simply assigning it to a new list, because with this method further modification done to the origin list won't be impacted to the copied one;
nums3 = list(nums)  # this method of copying does not escape origin modifications;
nums4 = nums[:]  # this is the same as above:

# fetching only unique values:
dublicated = [1, 2, 3, 4, 5, 5, 4, 3, 2, 1, 3, 2]
uniques = []
for val in dublicated:
    if val not in uniques:
        uniques.append(val)

list1 = [1, 2, 3, 4, 5]
list1 += [6, 7, 8, 9, 10]
list1.extend([11, 12, 13, 14, 15])
list1[5:5] = [True, False]  # picking a spot for insertion:
list1.sort(reverse=True)
# print(list1)

# sorting alphabetically:
friends = ["Ismoil", "Sorbon", "Somon", "Buzurg", "Umed", "Azam"]
friends[3:3] = ["afzal"]
friends.sort(key=str.lower)
# print(sorted(friends, reverse=True)) # this way we don't modify the original list:
# print(friends)

# -----------------------------------------------------------------

### Tuples:
# * Tuples are kinda list that their values and orders can not be changed:
tuples = (1, 2, 3)
alist = [4, 5, 6]
x, y, z = tuples  # unpacking tuples
a, b, c = alist  # unpacking lists

# tuple unpacking:
tuple1 = (1, 2, 3, 4, 5, 6, 7, 8, 9)
one, *two, three = tuple1
# print(one)
# print(two)
# print(three)

# -----------------------------------------------------------------

### Dictionaries - it is like an object in JS:
user = {
    "name": "ismoil",  # keys in dictionaries should be covered in "";
    "age": 25,
    "married": True,
}

# another way of creating dictionaries:
user2 = dict(name = "ismoil", age = 25, married = True)

key = user.get(
    "status", "married"
)  # this method returns "none" if the key does not exists, but we can give it a value right away in this get() method;

# print(type(user))
# print(len(user2)) # we can use len() method on dictionaries in Python;
# print(user.keys())
# print(user.values())
# print(user.items()) # getting keys/values as tuples;

has_key = "married" in user
# print(has_key)

user.update({"status": "married"}) # with this method we can create a new key/value pair or update an existing one;
# print(user)

## Copying:
# Bad Copy!!!
user3 = user2 # it creates new reference to same dictionary in the memory;
# Good Cpoy!!!
user4 = user2.copy()
user5 = dict(user2)

## Deletion:
removed1 = user.pop("status") # this one removes a key/value pair and returns the removed value as string;
# print(removed1, user)

removed2 = user.popitem() # this one removes a key/value pair and return the tuple of the removed key/value pair;
# print(removed2, user)

del user2["age"] # this way delete a key/value pair;
# print(user2)

del user2 # this way we delete a dictionary from our program entirely;
# print(user2) # we get error since user2 does not exist anymore after it has been deleted;

user.clear() # this one deletes all the keys/value pairs and returns an empty curly brackets;
# print(user)

# -----------------------------------------------------------------

### SETS:
set1 = {1, 2, 3, 4, 5, 6, 7, 8}
set2 = set(("ismoil", "umed", "sorbon"))

## No Duplicates are allowed in SETS - it just ignores them not throwing any errors:
set3 = {1, 2, 3, 3, 5, 5, 6}
# print(set3)

set_exists = 2 in set3 # checking 
# print(set_exists)

## You can not refer to an element in SETS by index of key:

## Adding a new element a set:
set1.add(9)
set1.update({10, 11, 12})
# print(set1)
unitied = set1.union(set2)
# print(unitied)
set4 = {5, 6, 8}
set5 = {9, 6, 4}
set4.intersection_update(set5) # keeps only the duplicates
# print(set4)
set4.symmetric_difference_update(set5) # keeps everything except the duplicates;
# print(set4)

# -----------------------------------------------------------------

### Functions
## !!! in Python we first define a function and then call it, the otherway gets you an error!!!
## !!! in Python By Default Functions return None Type, when in JS "undefined is returned" !!!
def sum(a, b, c = 10):
    return a + b + c

summed = sum(
    b=5, a=5
)  # this is called "Keyword Argument" which does not care about parameter positioning, but it has to come after postional argument;

## when we don't know how many parameters a function except:
def multi_param(*args): # it converts everything to tuple:
    print(args)
    print(type(args))

# multi_param(["dushanbe", "dubai", "moskow"])

def multi_names_param(**kwargs): # it converts everything to dictionary:
    print(kwargs)
    print(type(kwargs))

# multi_names_param(list_of_friends = ["dushanbe", "dubai", "moskow"])

##################################

## recursive function:
def recursive_function(num):
    if (num >= 10): return
    print(num)
    recursive_function(num + 1)

# recursive_function(0)

##################################

## "nonlocal" keyword:
def parent_func():
    name = "ismoil"

    def child_func():
        nonlocal name # it allows you to give new value to parent variables:
        name = "sorbon"
        print("from child: ", name)

    child_func()
    print("from parent: ", name)

# parent_func()

##################################

## Lambda functions | Anonymous functions:
square = lambda a, b: a * b
# print(square(3, 4))

# helpful usage of lambda functions:
def sum(x):
    return lambda y: print(x + y)

sum_ten = sum(10)
sum_twenty = sum(20)
# sum_ten(5)
# sum_twenty(5)

##################################

## Higher Order Functions:
list_of_numbers = [1, 2, 3, 4, 5, 6, 7, 8]

# mapping through list:
new_list_of_numbers = list(map(lambda x: x**x, list_of_numbers))
# print(new_list_of_numbers)

# filtering list:
list_of_even_nums = list(filter(lambda a: a % 2 == 0, list_of_numbers))
# print(list_of_even_nums)

# reduce function:
from functools import reduce
cities_names = ["Dushanbe", "Dubai", "New York", "Riyad", "Mekkah", "Medinah"]
total = reduce(lambda acc, cur: acc + len(cur), cities_names, 0)
# print(total)

# -----------------------------------------------------------------

### ERROR HANDLING = Try & Exceptions - something like "try and catch" in JS:
try:
  age = input("How old are you? ")
  
  if age == "":
    raise TypeError("You did not enter anything!\nPlease enter something!") # raising custom error:

  birth_year = 2023 - int(age)
  div_zero = 2023 / int(age)
  print("You were born in", birth_year)
  
except NameError:
    print("Something probably is undefined")
except ValueError:
  print("Please, enter numbers only")
except ZeroDivisionError:
  print("Please, type other numbers except zero - 0")
except Exception as error:
    print(error)
else: # this block runs after try if there are not any errors!!!
    print("No Error!!!")
finally: # this block runs no matter what happens!!!
    print("The end of try and error exception block code")

# -----------------------------------------------------------------

### Classes:
# creating class:
class Point:
    def __init__(
        self, x, y
    ):  # this constructor is called whenever a new instance of this class is created
        self.x = x
        self.y = y

    def move(self):
        print(f"moving: {self.x} and {self.y}")

    def draw(self):
        print(f"drawing: {self.x} and {self.y}")


# creating an instance:
point1 = Point(10, 15)
# print(point1.x)


# class inheritance:
class Line(Point):
    pass


# creating an instance of an inherited class:
line = Line(12, 13)
# print(line.x)

class Point3D(Point):
    def __init__(self, x, y, z):
        super().__init__(x, y)
        self.z = z
    
    def get_coordinates(self):
        return tuple(self.x, self.y, self.z)

# -----------------------------------------------------------------

### Working with Pathes:
# path = Path()
# all_files = path.glob("*")
# for file in all_files:
#   print(file)

# -----------------------------------------------------------------

### Ternary Operators: + using type() & isinstance():
ternary = 55
# print("it is string") if type(ternary) == str else print("it is not string")
# print("it is number") if isinstance(ternary, int) else print("it is not number")