# Write a program which will find all such numbers
# which are divisible by 7 but are not a multiple of 5,
# between 2000 and 3200(both included).
# The numbers obtained should be printed in a comma-seperated
# sequence on a single line


numberList = range(2000, 3201)
numberSequence = ""
count = 0
for number in numberList:
    if (((number % 7) == 0) and ((number % 5) != 0)):
        if(count != 0):
            numberSequence = numberSequence + ","
        numberSequence = numberSequence + str(number)
        count += 1
print(numberSequence)
