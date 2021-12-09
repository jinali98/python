
numbers = [1,5,9,9,7,5,4]


# add items to the end of the list
numbers.append(8)

# add item to a particular index
numbers.insert(0, 7)

# to remove an element
numbers.remove(8)

# to check a particular number is in the list 
print(1 in numbers)

# to sort the array
numbers.sort()

# to caclulate a specific element count
print(numbers.count(5))

# reverse the list
print(numbers.reverse())

# to make a copy of the list 
numbers2 = numbers.copy()
numbers2.append(8)
print(numbers2)

# to remove all the elements
# numbers.clear()

# tuples

tupleValue = (1,2,3)
# this is unpacking
x,y,z = tupleValue

print(len(tupleValue))

# dictionaries 
thisDict = {
    "name": "Jinali",
    "age": 23
}
thisDict["birthdate"] = "01/05/2021"
print(thisDict.get("date", "01/04/2021"))
print(thisDict)

