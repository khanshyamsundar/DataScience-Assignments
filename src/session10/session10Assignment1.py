# Read the dataset from the below link
# https://raw.githubusercontent.com/guipsamora/pandas_exercises/master/06_Stats/US_Baby_Names/US_Baby_Names_right.csv
# Questions:
# 1. Delete unnamed columns
# 2. Show the distribution of male and female
# 3. Show the top 5 most preferred names
# 4. What is the median name occurence in the dataset
# 5. Distribution of male and female born count by states


import pandas as pd
from pandasql import sqldf


def pysqldf(q): return sqldf(q, globals())


url = "https://raw.githubusercontent.com/guipsamora/pandas_exercises/master/"
url = url + "06_Stats/US_Baby_Names/US_Baby_Names_right.csv"
# read data
states_data = pd.read_csv(url)

# print top 5 rows
print(states_data.head())

# Delete unnamed columns
states_data_modified = states_data.loc[:, ~
                                       states_data.columns.str.contains('^Unnamed')]

# After removing Unnamed column
print(states_data_modified.head())

# Show the distribution of male and female
print("-"*100)
print("\n")
query1 = "select Gender, SUM(Count) as born_count from states_data_modified group by Gender"
print("Show the distribution of male and female")
print(pysqldf(query1))

# Show the top 5 most preferred names
print("-"*100)
print("\n")
query2 = "select Name, count(*) as Name_count, SUM(Count) as Total_Count "
query2 = query2 + "from states_data_modified group by Name order by Total_Count desc limit 5"
print("top 5 most preferred names")
print(pysqldf(query2))


# What is the median name occurence in the dataset
print("-"*100)
print("\n")
query3 = "select Name, Year, Gender, State, SUM(Count) as Total_Count from states_data_modified group by Name"
ds1 = pysqldf(query3)
median_value = ds1.median()
query4 = "select Name, Total_Count from ds1 where Total_Count="
query4 = query4 + str(median_value.Total_Count)
print("median name occurence in the dataset")
print(pysqldf(query4))


# Distribution of male and female born count by states
print("-"*100)
print("\n")
query5 = "select state, Gender, SUM(Count) as born_count from states_data_modified group by state, Gender"
print("Distribution of male and female born count by states")
print(pysqldf(query5))
