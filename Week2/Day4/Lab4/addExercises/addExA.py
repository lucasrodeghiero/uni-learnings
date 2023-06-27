yourString = str(input("Please input a string: "))
digit = 0
for word in yourString:
    if word.isdigit():
        digit += 1
print(f'String has: {digit} digits')
