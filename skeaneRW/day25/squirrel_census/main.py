import pandas

df = pandas.read_csv("skeaneRW/day25/squirrel_census/squirrel_data.csv")
'''
goal make a squirrel count csv including summary information based on:
Fur Color and Count
'''

fur_color = df["Primary Fur Color"]
summary = {
    "Fur Color": fur_color.unique(),
    "Count": [],
}

for color in summary["Fur Color"]:
    census_rows = df[df["Primary Fur Color"]== color]
    summary["Count"].append(len(census_rows))

for key, items in summary.items():
    print(key, items)

summary_df = pandas.DataFrame(summary)
summary_df = summary_df[summary_df["Count"] != 0]
summary_df.to_csv("skeaneRW/day25/squirrel_census/squirrel_count.csv")