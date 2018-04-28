# program which accepts a sequence of comma-separated numbers
# from console and generate a list

numberSeq = input("Please enter a sequence of coma-separated numbers: \n")
if numberSeq.count(",") != 0:
    numberList = numberSeq.split(",")
    numberList = list(map(lambda x: int(x), numberList))
else:
    print("Please enter coma-separated numbers")
print(numberList)
