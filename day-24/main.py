with open("my_text.txt") as file:
    content = file.read()
    print(content)

with open("my_text.txt", mode="w") as file:
    file.write("my_text.txt")
