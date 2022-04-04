from graphics import graphics
import random

def helper_quicksort():
    pass

def quicksort(input_data):
    less_than = []
    greater_than = []
    pivot = input_data[0]

    for val in input_data:
        print(val)
        if val > pivot:
            greater_than.append(val)
        else:
            #if val == pivot:
            #    continue
            less_than.append(val)

    if len(input_data) <= 1:
        print('QS: The length of the input data, ', end='')
        print(input_data, end = '')
        print(', is zero or one. Returning immediately.')

        print('QS: AFTER RECURSION...')
        print('    Original data:  ' + str(input_data))
        print('    Left (sorted):  ' + str(less_than))
        print('    Right (sorted): ' + str(greater_than))
        print('    Sorted data:    ' + (str(less_than) + str(pivot) + str(greater_than)))
        print('AFTER THE SORT: ' + (str(less_than) + str(pivot) + str(greater_than)))
        return less_than + [pivot] + greater_than

    else:
        less_than = quicksort(less_than)
        greater_than = quicksort(greater_than)
        print('QS: Data in:' + str(input_data))
        print('     Pivot:   ' + str(pivot))
        print('     Left:    ' + str(less_than))
        print('     Right:   ' + str(greater_than))


def main():
    print('Frames per second?   (Give 0 to disable animation.)')
    frame_speed = input()
    print('Please give the input data:')
    input_data = input()

    #if frame_speed == '0':
    #    frame_speed == False
    input_data = input_data.split()
    map_obj = map(int, input_data)
    input_data = list(map_obj)
    quicksort(input_data)


if __name__ == '__main__':
    main()

