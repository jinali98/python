numbers = [4,4,4,5,1,2,7, 7]
duplicate = []

for el in numbers:
    if el not in duplicate:
        duplicate.append(el)
   
# numbers.remove(4)
print(duplicate)


# first find the duplicate
# remove the duplicate