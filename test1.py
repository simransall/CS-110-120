# Write your code here :-)

def print_sorted(vals):
    for v in sorted(vals):
        print(v)

def print_sorted2(vals):
    vals2 = [int(v) for v in vals]
    for v in sorted(vals2):
        print(v)

def main():
    vals = ['0', '8', '-1', '5', '-3']
    print_sorted(vals)
    print('hello')
    print_sorted2(vals)

main()
