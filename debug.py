'''
Teaching a student how to debug

'''

if numbers.isdecimal() #check input
    return -1



def average(s):
    ''' (str) -> void #WARNING, docstring error, it should be (str) -> int
    Takes a string of digits as argument, and returns the average of the digits.
    If there are non-numerical characters in the string, return -1 instead.
    >>> average('48')
    6
    >>> average('abc123def')
    -1
    '''

    avg == 0 #compare, not assignment, should be =
    for i in range(len(numbers)):
        avg += i   #Warning usage error: avg += int(i)
        #add vertical space for better readability
    return avg / len(numbers)
    
if __main__ == '__name__': #style error: NuMs -> nums
    NuMs = input(Enter the digits) #input prompt not string "Enter the digits"
    print(average(NuMs))
