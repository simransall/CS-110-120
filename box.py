style = (input("Box style (light or dark or stripe): \n"))

print("+-----+")
if style == "light":
    print("|     |\n" * 3, end='')
elif style == "dark":
    print("|#####|\n" * 3, end='')
else:
    print("|#####|")
    print("|     |")
    print("|#####|")
print("+-----+")