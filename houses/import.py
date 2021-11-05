from cs50 import SQL
from sys import argv
from sys import exit
import csv

db = SQL("sqlite:///students.db")

if len(argv) != 2:
    print("Usage: python import.py csv")
    exit(1)

with open(argv[1]) as csvfile:
    reader = csv.reader(csvfile)
    next(reader) #Skip header CSV
    for student in reader:
        name = student[0].split(" ")
        first = name[0]
        if len(name) != 2:
            middle = name[1]
            last = name[2]
        else:
            middle = None
            last = name[1]
        house = student[1]
        birth = student[2]
        db.execute("INSERT INTO students (first, middle, last, house, birth) VALUES (:first, :middle, :last, :house, :birth)",
                    first=first, middle=middle, last=last, house=house, birth=birth)