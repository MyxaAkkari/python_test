simp_called = False # flag set to check if a function form simp module has been run or  not

def check_run():
    """Checks if any function from simp module has been run. returns True/False"""
    if simp_called:
        return True
    return False


def add_nums(n1, n2):
    """Takes two numbers and returns the sum"""
    global simp_called
    simp_called =True
    return n1 + n2


def sub_nums(n1, n2):
    """Takes two numbers and subtracts them (n1 - n2)"""
    global simp_called
    simp_called =True
    return n1 - n2
