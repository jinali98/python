user_input = input("> ")
words = user_input.split(" ")

emojis = {
    ":)" : "😊",
    ":(" : "😑"
}
output = ""
for each in words:
    output += emojis.get(each, each) + " "

print(output)