# Write a Python Program to print the given string in the format specified in the sample
# output.
# WE, THE PEOPLE OF INDIA, having solemnly resolved to constitute India into a
# SOVEREIGN, SOCIALIST, SECULAR, DEMOCRATIC REPUBLIC and to secure to all
# its citizens
# Sample Output:
# WE, THE PEOPLE OF INDIA,
#       having solemnly resolved to constitute India into a SOVEREIGN, !
#           SOCIALIST, SECULAR, DEMOCRATIC REPUBLIC
#               and to secure to all its citizens:


inputString = "WE, THE PEOPLE OF INDIA,<delimiter> having solemnly resolved to constitute India into a " +\
    "SOVEREIGN,<delimiter> SOCIALIST, SECULAR, DEMOCRATIC REPUBLIC <delimiter>" +\
    "and to secure to all its citizens"
delimiter = "<delimiter>"
inputStringList = inputString.strip().split(delimiter)
for index, item in enumerate(inputStringList):
    formatter = "\t"*index
    outputString = formatter + item if index != 1 else formatter + item + " !"
    print(outputString)
