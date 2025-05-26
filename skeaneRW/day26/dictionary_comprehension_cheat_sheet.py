'''
at its most basic, dictionary comprehension follows the format
to allows us to create new dictionaries from a list.
    new_dict = {new_key:new_value for item in list}

this can also be used to create a new dictionary from an existing dictionary:
    new_dict = {new_key:new_value for (key,value) in dict.items()}
'''
from random import randrange

student_names = ["todd","jeff","darcy","velma","stacy","horatio","sacha"]
#create student scores
student_dict = {name:randrange(0,100) for name in student_names}
#filter by students who got better than a 60.
passed_students = {key:value for (key,value) in student_dict.items() if value > 60}

print(student_dict)
print(passed_students)