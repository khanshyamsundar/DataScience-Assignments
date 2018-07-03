# This assignment is for visualization using matplotlib:
# data to use:
# url=
# https://raw.githubusercontent.com/Geoyi/Cleaning-Titanic-Data/master/titanic_original.csv'
# titanic = pd.read_csv(url)
# Charts to plot:
# 1. Create a pie chart presenting the male/female proportion
# 2. Create a scatterplot with the Fare paid and the Age, differ the plot color by gender

# %%
import pandas as pd
from pandasql import sqldf
import seaborn as sns
import matplotlib.pyplot as plot

url = 'https://raw.githubusercontent.com/Geoyi/Cleaning-Titanic-Data/master/titanic_original.csv'
# read data
titanic_data = pd.read_csv(url)
titanic_data.head()

# Requirement 1
# get male and female pasengers from dataset
male_passengers = titanic_data.loc[titanic_data.sex == 'male']
female_passengers = titanic_data.loc[titanic_data.sex == 'female']

# define sizes and labels for pie chart
sizes = [len(male_passengers), len(female_passengers)]
labels = ['Male', 'Female']
fig1, ax1 = plot.subplots()

# show pie chart to present male and female proportion on overall populations
ax1.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)
ax1.axis('equal')
plot.show()

# 2. Create a scatterplot with the Fare paid and the Age, differ the plot color by gender
sns.lmplot(x="age", y="fare", data=titanic_data, fit_reg=False, hue='sex', legend=True,
           palette=dict(male="#9b59b6", female="c"))
