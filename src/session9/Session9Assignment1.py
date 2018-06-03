# 1) How-to-count-distance-to-the-previous-zero
# For each value, count the difference back to the previous zero (or the start of the Series,
# whichever is closer)
# create a new column 'Y'
# Consider a DataFrame df where there is an integer column 'X'
# import pandas as pd
# df = pd.DataFrame({'X': [7, 2, 0, 3, 4, 2, 5, 0, 3, 4]})

import pandas as pd
import numpy as np

# create a pandas dataframe of given sequence
df = pd.DataFrame({'X': [0, 2, 0, 3, 4, 2, 5, 0, 3, 4]})

# find the indexs where number is non-zero
y = (df['X'] != 0)
#                     A               B                 C           y.groupby(C).cumsum()
# df      y       y.shift()       y!=y.shift()      B.cumsum()
# 0       0           NAN             1                 1                   0
# 2       1           0               1                 2                   1
# 0       0           1               1                 3                   0
# 3       1           0               1                 4                   1
# 4       1           1               0                 4                   2
# 2       1           1               0                 4                   3
# 5       1           1               0                 4                   4
# 0       0           1               1                 5                   0
# 3       1           0               1                 6                   1
# 4       1           1               0                 6                   2
df['Y'] = y.groupby((y != y.shift()).cumsum()).cumsum()
print('Sequences with count the difference back to the previous zero:\n')
print(df)

print("-"*100)


# 2) Create a DatetimeIndex that contains each business day of 2015 and use it to index a
# Series of random numbers.

bdRange = pd.date_range('1/1/2015', '12/31/2015', freq='B')
randNum = pd.Series(np.random.randn(len(bdRange)), index=bdRange)
print('Series of random numbers with date as index:\n')
print(randNum)

# Separator
print("-"*100)


# 3) Find the sum of the values in s for every Wednesday

df = pd.DataFrame({'numbers': np.random.randn(len(bdRange)), 'dates': bdRange})
totalValues_Wed = df[df['dates'].dt.weekday_name == 'Wednesday'].sum()
print("sum of the values in sequences for every Wednesday:\n")
print(totalValues_Wed)

# Separator
print("-"*100)


# 4) Average For each calendar month

# Set a new column of month of each dates
df['month'] = df['dates'].dt.month

# apply group by to select each calender month and then apply mean() to get the average of each month
avgCalenderMonth = df.groupby('month').mean()

# print the data
print('Average For each calendar month is:\n')
print(avgCalenderMonth)

# Separator
print("-"*100)

# 5) For each group of four consecutive calendar months in s, find the date on which the
# highest value occurred.

# create group on consecutive 4 months
df['monthGrp'] = df['month'].apply(lambda x: np.floor((x/4)) - 1
                                   if x % 4 == 0 else np.floor((x/4)))
df2 = df.loc[df.groupby('monthGrp')['numbers'].idxmax()]
print(df2)
