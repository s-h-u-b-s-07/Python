ListOfString = ["Apple", "Mango","Banana", "Pineapple"]
search = 'Apple'
index = []
i = 0
length = len(ListOfString)

while i < length:
    if search == ListOfString[i]:
        index.append(i)
    i += 1

print(f'{search} is present in string at index {index}')