
def shape_alpha():
    outer_list = ['','']
    outer_list[0] = [10, "abc", "jkl", 40]
    outer_list[1] = ['', '']
    outer_list[1][0] = [1.1, -17]
    outer_list[1][1] = [123, 456]
    return outer_list

def shape_bravo():
    outer_list = ['','']
    outer_list[0] = ['','']
    outer_list[1] = ['','']
    outer_list[0][0] = ['', '']
    outer_list[0][0][0] = "whoa"
    outer_list[0][0][1] = "excellent"

    outer_list[0][1] = ['', '']
    outer_list[1][0] = outer_list[0][1]
    outer_list[0][1][0] = "bogus"
    outer_list[1][0][1]= "righteous"

    outer_list[1][1] = "rufus"
    return outer_list

def shape_charlie(arg1):
    outer_list = ['', '']
    outer_list[0] = ['', '']
    outer_list[0][0] = ['', '']
    outer_list[0][1] = arg1
    outer_list[0][0][0] = ['', '']
    outer_list[0][0][1] = arg1
    outer_list[0][0][0][0] = None
    outer_list[0][0][0][1] = arg1
    outer_list[1] = arg1
    return outer_list

def shape_delta(arg1, arg2):
    outer_list = [arg1, arg2, '', '']
    outer_list[2] = [arg1, '', '', arg2]
    outer_list[2][1] = [arg1, arg2, '', '']
    outer_list[2][1][2] = [arg1, arg2]
    outer_list[2][1][3] = [30]
    outer_list[2][2] = [20]
    outer_list[3] = [10]
    return outer_list

def shape_echo(arg1, arg2, arg3):
    outer_list = ['', '']
    outer_list[0] = ['', '']
    outer_list[0][0] = ['', '']
    outer_list[0][0][0] = outer_list
    outer_list[0][0][1] = arg3
    outer_list[0][1] = arg2
    outer_list[1] = arg1
    return outer_list
