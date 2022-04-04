from list_insert import *


def main():
    obj = ListNode((1,2))
    obj2 = ListNode((3,8))

    data = sorted_list_insert(None, obj)
    data = sorted_list_insert(data, obj2)
    print_list(data)


if __name__ == '__main__':
    main()