'''
# without pandas

import csv
with open("skeaneRW/day25/intro_to_pandas/weather.csv",mode="r") as file:
    data = csv.reader(file)
    temps = []
    for line in data:
        if line[1].isdigit():
            temps.append(int(line[1]))
    print(temps)

# all of this (👆) can be done in a single line using pandas.
df = pandas.read_csv("skeaneRW/day25/intro_to_pandas/weather.csv")
'''

import pandas
df = pandas.read_csv("skeaneRW/day25/intro_to_pandas/weather.csv")
# you can convert a dataFrame to a dict
temp_dict = df.to_dict()
print(temp_dict)

# you can convert a series to a list.
temp_list = df["temp"].to_list()
avg_temp = sum(temp_list)/len(temp_list)
print(avg_temp)

# using pandas you can just use built in fns
print(df["temp"].mean()) # get average
print(df.temp.max()) # can also use dot notation and different built in fns

#target a row
print(df[df.day == "Monday"]) # returns matching row
print(df[df.temp == 62]) # returns multiple rows if more than one match
min_temp = df.temp.min()
print(df[df.temp == min_temp]) #can target rows using series fns or other variables
print(df[df.day.str.startswith('T')]) #has built in fns to refine searching on Series headings
monday = df[df.day == "Monday"]
def convert_to_celcius(temp):
    return round((temp - 32) * 5/9, 1)
print(f"the temp on monday is {convert_to_celcius(monday.temp[0])}C")

# create a dataframe from scratch:
scoobies = {
    "name": ["scooby", "shaggy", "fred", "daphne", "velma"],
    "likes": [
        ["snacks"],
        ["snacks"], 
        ["traps","ascots","mysteries"], 
        ["fashion","luring monsters","mysteries"], 
        ["books","nerd stuff","mysteries"],
        ],
    "age": [3, 19, 20, 18, 17],
}
scoob_df = pandas.DataFrame(scoobies)
print(scoob_df.head(2)) # for large data sets it can be useful to use .head() to preview a limited number of rows.
print(scoob_df.name)

#to create a csv from your new dataframe use .to_csv() and include your new file path...
scoob_df.to_csv("skeaneRW/day25/intro_to_pandas/scoobies.csv")

