# Problem Statement​ ​1:
# Write a Python Program to implement your own myreduce() function which works exactly
# like Python's built-in function reduce()


def multiplier(x, y):
    return x*y


def addition(x, y):
    return x+y

# Custom myreduce function


def myreduce(functionName, collection, initials=None):
    result = None
    bufferCollection = []
    if initials is not None:
        bufferCollection.append(initials)
        bufferCollection = bufferCollection + collection[:]
    else:
        bufferCollection = collection[:]
    if(len(bufferCollection) > 0):
        result = bufferCollection[0]
        for item in bufferCollection[1:]:
            result = functionName(result, item)
        return result
    else:
        raise TypeError("myreduce() of empty sequence with no initial value")


data = [1, 4, 6, 2, 5, 8, 4]
# test 1 using custom multiplier function
output1 = myreduce(multiplier, data)

# test 2 using custom addition function
output2 = myreduce(addition, data)

# test 3 using custom addition function with initials data
output3 = myreduce(addition, data, 3)

# test 4 using anonymous fucntion(lambda expression)
output4 = myreduce(lambda a, b: a if (a > b) else b, data)

# print results
print("Multiplied: %d" % output1)
print("Added: %d" % output2)
print("Added with initials: %d" % output3)
print("Maximum no: %d" % output4)

# separator
print("-"*100)

# Problem Statement​ ​2:
# Write a Python program to implement your own myfilter() function which works exactly
# like Python's built-in function filter()


# Custom filter function
def myfilter(function, collection):
    filteredCollection = []
    for item in collection:
        if(function(item)):
            filteredCollection.append(item)
    return filteredCollection


# test result from custom myfilter function
# Test 1 using anonymous fucntion(lambda expression)
numberList = range(-5, 5)
lessThanZero = myfilter(lambda x: x < 0, numberList)
print(lessThanZero)

# Test 2 using custom funcion named filterVowels whih will filter vowels from any alphabet list
# function that filters vowels


def filterVowels(alphabet):
    vowels = ['a', 'e', 'i', 'o', 'u']
    if(alphabet in vowels):
        return True
    else:
        return False


alphabets = ['a', 'b', 'd', 'e', 'i', 'j', 'o']
filteredVowels = myfilter(filterVowels, alphabets)

print(filteredVowels)
