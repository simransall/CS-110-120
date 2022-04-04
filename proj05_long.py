''' File: proj05_long.py
    Author: Simran Sall
    Purpose: Multiple functions that iterate through linked lists
        to visually display them as well as determine if the linked
        list is sorted, and the sum of all the values of each node.
'''

from list_node import *

def is_sorted(head):
    ''' This function determines if each value of the node fork
        the linked list is sorted
        Arguments: head is the first node of the list
        Return Value: will return True if sorted, False if not sorted
        Pre-Condition: none
    '''
    cur = head
    while cur is not None:
        if cur.next is None:
            return True
        # if current val is greater than the next val, return False
        if cur.val > cur.next.val:
            return False
        cur = cur.next
    return True

def list_sum(head):
    ''' This function adds all of the node values together and
        returns the total sum
        Arguments: head is the first node of the list
        Return Value: will return the total sum of the values
        Pre-Condition: none
    '''
    total_sum = 0
    cur = head
    if head is None:
        total_sum = 0
    while cur is not None:
        # add each current value to the total amount
        total_sum += cur.val
        cur = cur.next
    return total_sum

def pair(list1, list2):
    ''' This function iterates through two linked lists and
        returns a new linked list that consists of tuples with
        values from each linked list. The new linked list is the
        length of the shortest linked list between list1 and list2
        Arguments: list1 and list2 are the linked lists that the
            function will be iterating over
        Return Value: a new linked list with each node being a tuple
            of the nodes from list1 and list2
        Pre-Condition: None
    '''
    if list1 is None:
        return None
    if list2 is None:
        return None
    # initialize the return value
    retval = None
    # since we are adding at the tail, set the tail to be the return val
    tail = retval
    cur = list1
    cur2 = list2
    while cur is not None and cur2 is not None:
        # set the tuple for each node
        pairs = (cur.val, cur2.val)
        # add that tuple to a new linked list
        new = ListNode(pairs)
        if retval is None:
            # set the return value to the new linked list
            retval = new
            # reset the tail so it is not None
            tail = retval
        else:
            # continue adding values to new linked list
            tail.next = new
            tail = tail.next
        cur = cur.next
        cur2 = cur2.next
    return retval

def print_pair_partial(list1, list2):
    '''This function iterates through two linked lists and
        prints a visual of the new linked list that consists
        of tuples with values from each linked list. The new
        linked list is the length of the longest list between
        list 1 and 2. The shortest list of the two will just print
        out 'None' if there are no more values left.
        Arguments: list1 and list2 are the linked lists that the
            function will be iterating over
        Return Value: a printed visual that represents the new
            linked list with '1' being the node from list1 and
            '2' being the node from list2
        Pre-Condition: None
    '''
    # initialize the return value
    retval = None
    # since we are adding at the tail, set the tail to be the return val
    tail = retval
    cur = list1
    cur2 = list2
    while cur is not None or cur2 is not None:
        # set the tuples that consist of each node
        if cur is None:
            pairs = (None, cur2.val)
        elif cur2 is None:
            pairs = (cur.val, None)
        else:
            pairs = (cur.val, cur2.val)
        # create a new linked list of the tuple above
        new = ListNode(pairs)
        # add to linked list
        if retval is None:
            retval = new
            tail = retval
        else:
            tail.next = new
            tail = tail.next
        # print out values
        if cur is None:
            print('1: ' + 'None' + '   2: ' + str(cur2.val))
        elif cur2 is None:
            print('1: ' + str(cur.val) + '   2: ' + 'None')
        else:
            print('1: ' + str(cur.val) + '   2: ' + str(cur2.val))
        # ensure that loop will not terminate if list1 or list2 is null
        if cur is not None:
            cur = cur.next
        if cur2 is not None:
            cur2 = cur2.next
    return retval

def pair_partial(list1, list2):
    '''This function iterates through two linked lists and
        returns a new linked list that consists
        of tuples with values from each linked list. The new
        linked list is the length of the longest list between
        list 1 and 2. The shortest list of the two will just print
        out 'None' if there are no more values left.
        Arguments: list1 and list2 are the linked lists that the
            function will be iterating over
        Return Value: a printed visual that represents the new
            linked list with '1' being the node from list1 and
            '2' being the node from list2
        Pre-Condition: None
    '''
    # initialize the return value
    retval = None
    # since we are adding at the tail, set the tail to be the return val
    tail = retval
    cur = list1
    cur2 = list2
    while cur is not None or cur2 is not None:
        if cur is None:
            pairs = (None, cur2.val)
        elif cur2 is None:
            pairs = (cur.val, None)
        else:
            pairs = (cur.val, cur2.val)
        # set a new linked list with the node being the tuple
        new = ListNode(pairs)
        # add to linked list
        if retval is None:
            retval = new
            tail = retval
        else:
            tail.next = new
            tail = tail.next
        # ensure that loop will not terminate if list1 or list2 is null
        if cur is not None:
            cur = cur.next
        if cur2 is not None:
            cur2 = cur2.next
    return retval
