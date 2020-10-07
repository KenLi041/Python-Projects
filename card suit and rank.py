#Ken Li 260823059  #q3 card

"""
Type contract: It takes an int input and return an int output between 0 and 3
example1
>>> get_suit(7)
2
example2
>>> get_suit(8)
3
example3
>>> get_suit(10)
1
"""

def get_suit(card):
    if card%4 == 1:
        return 0
    elif card%4 == 2:
        return 1
    elif card%4 == 3:
        return 2
    elif card%4 == 0:
        return 3
    else: return ''
    
"""
Type contract: it takes an int input and return an int output between 0 and 12
example1
>>> get_rank(7)
1
example2
>>> get_rank(8)
1
example3
>>> get_rank(17)
4
"""
    
def get_rank(card):
    if card == 0:
        return 0
    elif card%4 == 0:
        return int((card/4) - 1)
    else:
        return int(card/4)
    
"""
Type contract: it takes 2 int input and return a boolean output between true (same rank) and false (not same rank)
example1
>>> same_rank(1, 3)
True
example2
>>> same_rank(7, 3)
False
example3
>>> same_rank(21, 13)
False

"""

def same_rank(card1, card2):
    if get_rank(card1) == get_rank(card2):
        return True
    else: return False
    
"""
Type contract: it takes 2 int input and return a boolean output between true (same suit) and false (not same suit)
example1
>>> same_suit(7, 15)
True
example2
>>> same_suit(8, 16)
True
example3
>>> same_suit(6, 25)
False
"""
    

def same_suit(card1, card2):
    if get_suit(card1) == get_suit(card2):
        return True
    else: return False
    
"""
Type contract: it takes 2 int input and return a boolean output between true (same color suit) and false (not same color suit)
example1
>>> same_color_suit(5, 6)
True
example2
>>> same_color_suit(15, 26)
False
example3
>>> same_color_suit(25, 46)
True
"""
    
def same_color_suit(card1, card2):
    if (get_suit(card1) == 0) and (get_suit(card2) == 0):
        return True
    elif ((get_suit(card1) == 0) and (get_suit(card2) == 1)):
        return True
    elif ((get_suit(card1) == 1) and (get_suit(card2) == 0)):
        return True
    elif ((get_suit(card1) == 1) and (get_suit(card2) == 1)):
        return True
    elif ((get_suit(card1) == 2) and (get_suit(card2) == 2)):
        return True
    elif ((get_suit(card1) == 2) and (get_suit(card2) == 3)):
        return True
    elif ((get_suit(card1) == 3) and (get_suit(card2) == 2)):
        return True
    elif ((get_suit(card1) == 3) and (get_suit(card2) == 3)):
        return True
    else: return False
