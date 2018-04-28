# Implement​ ​a​ ​function​ ​longestWord()​ ​that​ ​takes​ ​a​ ​list​ ​of​ ​words​ ​and​ ​returns​ ​the​ ​longest one.
from functools import reduce


def longestWord(wordList):
    return reduce(lambda a, b: a if (len(a) > len(b)) else b, wordList)


inputList = ["Workspace", "thisisaveryverybigword",
             "Assignments", "datasciences", "comprehension"]
longestWordName = longestWord(inputList)
print(longestWordName)
