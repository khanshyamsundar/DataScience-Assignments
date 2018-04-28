# Create the below pattern using nested for loop in Python.

# *
# * *
# * * *
# * * * *
# * * * * *
# * * * *
# * * *
# * *
# *
innerUpperBound = 0
for outerIndex in range(0, 9):
    # after 4th index number of * is decreasing
    innerUpperBound = innerUpperBound+1 if outerIndex < 5 else innerUpperBound-1
    value = ""
    for innerIndex in range(0, innerUpperBound):
        value = value + "* "
    # remove the extra space at the last of each value
    value = value[0:-1]
    print(value)
