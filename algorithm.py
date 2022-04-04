# Write your code here :-)

def algorithm(string):
    i = 0
    total = 0
    j = 0
    maximum = 0
    while j <= len(string)-3:
        for k in string[i:i+3]:
            total += int(k)
        if maximum < total:
            maximum = total
        i += 1
        j += 1
        total = 0
    print(maximum)


def main():
    string = '1847209901'
    new_string = '1234567'
    algorithm(new_string)

main()
