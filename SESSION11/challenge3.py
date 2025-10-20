# Challenge 3

"""
Write a program that will complete a line by randomly selecting
words from specific files.

The line completing is as follows:
My name is <NAME>, and I am absolutely <FEELING> to learn Python on <DAY>.

The files already created are: name.txt, feeling.txt, day.txt

Open the files and read contents, select a random line from each file,
and then complete the line above and print it to the console.
"""

import random

with open("name.txt", "r") as file:
    names = file.readlines()
    name = random.choice(names).strip()
    file.close()

with open("feeling.txt", "r") as file:
    feelings = file.readlines()
    feeling = random.choice(feelings).strip()
    file.close()

with open("day.txt", "r") as file:
    days = file.readlines()
    day = random.choice(days).strip()
    file.close()

print(f"My name is {name}, and I am absolutely {feeling} to learn Python on {day}")