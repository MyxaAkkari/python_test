from tools.numbers.simp import check_run 
# importing check_run() function to check if any func has been run from simp module first


def sumofdigits(num):
    """Takes a number, returns the sum of the digits of the number"""
    if check_run():
        sum = 0 
        for digit in str(num): # converting the num to a string then looping through the digits 
            sum += int(digit) # converting back to int in order to be able to add the numbers
        return sum
    else: raise Exception("At least one function from simp module needs to be called first.") #Exception error

def ispal(num):
    """Takes a number, checks if number is a plaindrome. returns True/False."""
    if check_run():
        num = str(num)
        if num == num[::-1]: # checks if num is equal to reversed num
            return True
        else: 
            return False
    else: raise Exception("At least one function from simp module needs to be called first.")


