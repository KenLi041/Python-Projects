
"""
string = ""
newstring = string.replace(" ", "") #Eliminate white space"""


def is_Palindrome(string):
    string = string.lower#convert string to lower case
    
    for char in string: #Eliminate white space using for loop!
        if char != " ":
            newstring += char
    
    if newstring == newstring[::-1]:
        return True
    else:
        return False

