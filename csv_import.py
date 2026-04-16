import csv

with open("test.csv", "r", encoding = "utf-8") as file:
    students = csv.reader(file)
    
    for student in students:
        print(student)

with open("test.csv", "r", encoding = "utf-8") as file:
    students = csv.DictReader(file)

    for student in students:
        print(student)