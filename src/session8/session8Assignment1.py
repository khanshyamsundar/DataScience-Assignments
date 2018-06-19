# We have the min and max temperatures in a city In India for each months of the year.
# We would like to find a function to describe this and show it graphically, the dataset
# given below.
# Task:
# 1. fitting it to the periodic function
# 2. plot the fit
# Data
# Max = 39, 41, 43, 47, 49, 51, 45, 38, 37, 29, 27, 25
# Min = 21, 23, 27, 28, 32, 35, 31, 28, 21, 19, 17, 18

# %%
import numpy as np
import matplotlib.pyplot as plt
from scipy import optimize

# import data as a numpy array
temp_max = np.array([39, 41, 43, 47, 49, 51, 45, 38, 37, 29, 27, 25])
temp_min = np.array([21, 23, 27, 28, 32, 35, 31, 28, 21, 19, 17, 18])

# set 12 months to use it as x-axis
months = np.arange(12)

# Set a evenly spaced numbers to plot the periodic function
days = np.linspace(0, 12, num=365)

# define the periodic function


def yearly_temps(times, avg, ampl, time_offset):
    return (avg + ampl * np.cos((times + time_offset) * 2 * np.pi / times.max()))


# fitting it to the periodic function
res_max, cov_max = optimize.curve_fit(yearly_temps, months, temp_max)
res_min, cov_min = optimize.curve_fit(yearly_temps, months, temp_min)

# plot the fit
plt.plot(months, temp_max, 'ro')
plt.plot(days, yearly_temps(days, *res_max), 'r-')
plt.plot(months, temp_min, 'bo')
plt.plot(days, yearly_temps(days, *res_min), 'b-')
plt.xlabel('Month')
plt.ylabel('Min and max temperature')
plt.show()
