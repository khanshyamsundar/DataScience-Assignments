# Problem​ ​Statement​ ​1:
# Implement a Python program to generate all sentences where subject is in
# ["Americans", "Indians"] and verb is in ["Play", "watch"] and the object is in
# ["Baseball","cricket"].
# Hint: Subject,Verb and Object should be declared in the program as shown below.
# subjects=["Americans ","Indians"]
# verbs=["play","watch"]
# objects=["Baseball","Cricket"]
# Output should come as below:
# Americans play Baseball.
# Americans play Cricket.
# Americans watch Baseball.
# Americans watch Cricket.
# Indians play Baseball.
# Indians play Cricket.
# Indians watch Baseball.
# Indians watch Cricket.


subjects = ["Americans", "Indians"]
verbs = ["play", "watch"]
objects = ["Baseball", "Cricket"]
outputSentenceArray = [(a + " " + b + " " + c+".")
                       for a in subjects for b in verbs for c in objects]
for sentence in outputSentenceArray:
    print(sentence)
