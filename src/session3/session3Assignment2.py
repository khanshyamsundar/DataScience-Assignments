# Implement​ ​List​ ​comprehensions​ ​to​ ​produce​ ​the​ ​following​ ​lists.
# Write​ ​List​ ​comprehensions​ ​to​ ​produce​ ​the​ ​following​ ​Lists

# ['A',​ ​'C',​ ​'A',​ ​'D',​ ​'G',​ ​'I',​ ​’L’,​ ​‘​ ​D’]
inputString1 = "ACADGILD"
outputArray1 = [x for x in inputString1]
print(outputArray1)

# ['x',​ ​'xx',​ ​'xxx',​ ​'xxxx',​ ​'y',​ ​'yy',​ ​'yyy',​ ​'yyyy',​ ​'z',​ ​'zz',​ ​'zzz',​ ​'zzzz']
inputString2 = "xyz"
outputArray2 = [(a*b) for a in inputString2 for b in range(1, 5)]
print(outputArray2)

# ['x',​ ​'y',​ ​'z',​ ​'xx',​ ​'yy',​ ​'zz',​ ​'xx',​ ​'yy',​ ​'zz',​ ​'xxxx',​ ​'yyyy',​ ​'zzzz']
inputString3 = "xyz"
outputArray3 = [(a*b) for a in range(1, 5) for b in inputString3]
print(outputArray3)

# [[2],​ ​[3],​ ​[4],​ ​[3],​ ​[4],​ ​[5],​ ​[4],​ ​[5],​ ​[6]]
outputArray4 = [[(b+a)] for a in range(0, 3) for b in range(2, 5)]
print(outputArray4)


# [[2,​ ​3,​ ​4,​ ​5],​ ​[3,​ ​4,​ ​5,​ ​6],​ ​[4,​ ​5,​ ​6,​ ​7],​ ​[5,​ ​6,​ ​7,​ ​8]]
outputArray5 = [[(b+a) for a in range(0, 4)] for b in range(2, 6)]
print(outputArray5)


# [(1,​ ​1),​ ​(2,​ ​1),​ ​(3,​ ​1),​ ​(1,​ ​2),​ ​(2,​ ​2),​ ​(3,​ ​2),​ ​(1,​ ​3),​ ​(2,​ ​3),​ ​(3,​ ​3)]
inputNumber6 = [1, 2, 3]
pairNumbers = [(x, y) for y in inputNumber6 for x in inputNumber6]
print(pairNumbers)
