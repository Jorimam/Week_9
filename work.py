'''
students = [
    {"id": 1, "name": "Alice", "score": 78},
    {"id": 2, "name": "Bob", "score": 45},
    {"id": 3, "name": "Charlie", "score": 92},
    ...
 ]
'''
import random
students = []

items = 1
while items <= 1000:
    items += 1
    name = "jo"
    records = {"id": items, "name":(f"student{items + 1}") , "score":random.randint(25, 100)}
    students.append(records)
print(students)

