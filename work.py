'''
 Generating students ID, name and random scores as a dictionary in a list
'''
import random
students = []

items = 1
while items <= 1000:
    items += 1
    name = "jo"
    records = {"id": items, "name":(f"student{items + 1}") , "score":random.randint(25, 100)}
    students.append(records)
#print(students)

#Step 2
i = 0 
condition = True
while condition:
    if i < 10:
        i += 1
        print(i)   
    else:
        condition = False
