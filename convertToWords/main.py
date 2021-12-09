numbers = {
    "1" : "one",
    "2" : "two",
    "3" : "three",
    "4" : "four",
}

output = ''

phone = input('Phone: ')
for each in phone:
    output += numbers.get(each) + " "

print(output)