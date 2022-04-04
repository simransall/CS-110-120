from list_node import *

def reverse_list(old_head):
    cur = old_head
    prev_node = None
    print('--- BEFORE THE LOOP ---')
    print('original list: ' + str(old_head) + '\n\n')
    while cur is not None:
        next = cur.next
        cur.next = prev_node
        prev_node = cur
        cur = next
        print('old: ' + str(cur))
        print('new: ' + str(prev_node))
    old_head = prev_node
    return prev_node

def accordion(old_head):
    cur = old_head
    count = 0
    if old_head is None:
       return None
    else:
        while cur.next is not None:
            count += 1
            if count % 2 == 1:
                cur = cur.next.next
            else:
                cur = cur.next
    return cur

def insert_at(old_head, new_node, pos):
    cur = old_head
    count = 0
    if pos == 0:
        if old_head is None:
            old_head = new_node
            return old_head
        else:
            old_head = new_node
            return old_head
    else:
        old_head.next = new_node
        return new_node

def too_many_aliases():
    outer_list = ['', '', '', '']
    outer_list[0] = ['', '']
    outer_list[0][0] = [11, 22]
    outer_list[0][1] = [33, 44]
    outer_list[1] = ['', '']
    outer_list[1][0] = outer_list[0][0]
    outer_list[1][1] = outer_list[0][1]
    outer_list[2] = outer_list[0]
    outer_list[3] = outer_list[1]
    return outer_list
