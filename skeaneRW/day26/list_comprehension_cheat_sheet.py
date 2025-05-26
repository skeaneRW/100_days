'''
list comprehension allows you to make a list from another list.

This can be more concise than a traditional for loop.
'''
# with for loop:
numbers = [1,2,3,4,5]
new_numbers = []
for num in numbers:
    new_numbers.append(num + 1)
print(new_numbers)
# with list comprehension you could write the same statement in one line:
new_numbers = [num + 1 for num in numbers]
print(new_numbers)

# we can also add an if condition to list comprehension.
new_numbers = [num + 1 for num in numbers if num % 2 == 0]
print(new_numbers)

# list comprehensions can be used with multiple types of lists.
names = ["ted","larry","bob","beth","agusto","pierre","felicia"]
short_names = [name for name in names if len(name) <= 4]
print(short_names)

foods = {"fruits":["apple", "lemon", "grape"], "veg":["turnip", "sprouts", "eggplant"]}
new_foods = [{key: value} for key, value in foods.items() if key == "fruits"]
print(new_foods)

# we can add if else conditions as well...
new_numbers = [num + 1 if num % 2 == 0 else '-' for num in numbers]
print(new_numbers)

#for loop vs list_comprehension:
vowels = ['a','e','i','o','u']
some_vowels = ['a','e']
missing_vowels = []
for vowel in vowels:
    if vowel not in some_vowels:
        missing_vowels.append(vowel)
print(missing_vowels)

new_missing_vowels = [v for v in vowels if v not in some_vowels]
print(new_missing_vowels)
