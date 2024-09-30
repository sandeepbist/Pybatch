#Lambda Function adding two nnumbers
add = lambda a,b:a+b
print(add(3,5))

numbers = [1,2,3,4]
squared = map(lambda x: x * x, numbers)
print(list(squared))

#write a program to multiply two variables using lambda funcion
mult = lambda a,b : a*b
print(mult(5,10))

# wirte a program to square a each number in a list without using map and lambda

even = filter(lambda x:x % 2 == 0,numbers)
print(list(even))

# write a program to create a list of squares of even number from 0 to 9
sq = [ ]
for i in range(10):
    if i% 2 == 0:
        sq.append(i**2)
print("using loop",sq)

#using list comprehension
sq2 = [i ** 2 for i in range(10) if i % 2 ==0]
print("using List comprehension",sq2)



# Write a program that prints current time then pause for few seconds and again prints current time.

import time
from datetime import datetime

def print_current_time():
    while True:
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        print(f"Current Time: {current_time}")
        
        time.sleep(5)

print_current_time()

# write a program that takes directory address from user and returns a list of files and directories in that address

import os

def list_files_and_directories(directory_path):
    try:
        items = os.listdir(directory_path)
        print(f"Files and directories in '{directory_path}':")
        return items
    except FileNotFoundError:
        print("Directory not found.")
        return []

directory_path = input("Enter the directory path: ")
items = list_files_and_directories(directory_path)
for item in items:
    print(item)
