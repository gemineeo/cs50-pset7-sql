from cs50 import SQL
from sys import argv
from sys import exit
import csv

db = SQL("sqlite:///students.db")

if len(argv) != 2:
    print("Usage: python roster.py house")
    exit(1)

house = argv[1]

students = db.execute("SELECT * FROM students WHERE house = :house ORDER BY last, first ASC",
                          house=house)

for student in students:
    first = student["first"]
    middle = student["middle"]
    last = student["last"]
    birth = str(student["birth"])
    if middle != None:
        name = first + " " + middle + " " + last
    else:
        name = first + " " + last
    print(name + ", born " + birth)