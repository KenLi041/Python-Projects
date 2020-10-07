#Ken Li 260823059  #q1 smoothie

#Careful remove all function calls and main body of program! Function only!

#first define each of four smoothie types, sizes and toppings in global variables at top                                                                                                                                                                                                                                                                                                                                                                                                                                     
"""WARNING! IF YOU CALLED THE SEPARATE FUNCTION print_receipt(subtotal, SMOOTHIE1_NAME, SIZE4_NAME, TOPPING4_NAME)
AND GOT ERROR THAT'S BECAUSE THE PDF GIVEN EXAMPLE STRESSES THE NEED TO COMMANDLINE ENTER A SUBTOTAL VALUE FIRST!
I DID WHAT YOUR PDF ASKED LIKE IN THE EXAMPLE GIVEN!
IF YOU GOT AN ERROR THAT"S CUZ YOU DIDN"T ASSIGN SUBTOTAL VALUE! PLEASE ENTER SUBTOTAL VALUE IN COMMANDLINE FIRST BEFORE USING THAT FUNCTION!"""

SMOOTHIE1_NAME = "Pineapple Banana"
SMOOTHIE1_COST = 4.99
SMOOTHIE2_NAME = "Almond Basil"
SMOOTHIE2_COST = 6.49
SMOOTHIE3_NAME = "Purple Surprise"
SMOOTHIE3_COST = 0.99
SMOOTHIE4_NAME = "Onion Toffee"
SMOOTHIE4_COST = 9.99
SIZE1_NAME = "small"
SIZE1_COST = -2
SIZE2_NAME = "medium"
SIZE2_COST = 0
SIZE3_NAME = "large"
SIZE3_COST = 2
SIZE4_NAME = "galactic"
SIZE4_COST = 100
TOPPING1_NAME = "no topping"
TOPPING1_COST = 0
TOPPING2_NAME = "cinnamon"
TOPPING2_COST = 1
TOPPING3_NAME = "chocolate shavings"
TOPPING3_COST = 1
TOPPING4_NAME = "shredded coconut"
TOPPING4_COST = 1

""" This function takes 9 arguments, 4 strings & 4 floats for potential answers and costs, options should be separated!
It presents question to user and display 4 options & costs each on own line, then ask for input and return 'you have selected' with options corresponding to different questions
# if users not enter right number or string return empty string
# use \t for tab, \n for new line
Example1
>>> x = pose_question_with_costs("Which size would you like?", "small", -2.0, "medium", 0.0,
                                 "large", 2.0, "galactic", 100.0)
Which size would you like? 
1)   -2      small 
2)   0   medium 
3)   2   large 
4)   100     galactic
Your choice (1-4): 3
You have selected large
>>> print(x)
large

Example2
>>> x = pose_question_with_costs("Which size would you like?", "small", -2.0, "medium", 0.0,
                                 "large", 2.0, "galactic", 100.0)
Which size would you like? 
1)   -2      small 
2)   0   medium 
3)   2   large 
4)   100     galactic
Your choice (1-4): 2
You have selected medium
>>> print(x)
medium

Example3
>>> x = pose_question_with_costs("Which size would you like?", "small", -2.0, "medium", 0.0,
                                 "large", 2.0, "galactic", 100.0)
Which size would you like? 
1)   -2      small 
2)   0   medium 
3)   2   large 
4)   100     galactic
Your choice (1-4): 1
You have selected small
>>> print(x)
small
"""


def pose_question_with_costs(question, option1, cost1, option2, cost2, option3, cost3, option4, cost4):
    option1 = SIZE1_NAME 
    cost1 = SIZE1_COST
    option2 = SIZE2_NAME 
    cost2 = SIZE2_COST
    option3 = SIZE3_NAME 
    cost3 = SIZE3_COST
    option4 = SIZE4_NAME   #print question
    cost4 = SIZE4_COST
    print (question, "\n1)\t", cost1, "\t", option1, "\n2)\t", cost2, "\t", option2, "\n3)\t", cost3, "\t", option3,"\n4)\t", cost4, "\t", option4)
    
    userinput1 = input("Your choice (1-4): ")  #prompt input
    try: choice1 = int(userinput1)
    except ValueError:
        print("Sorry, that is not a valid option.") #prevent bad user input
    if choice1 == 1:
        print ("You have selected", option1)  #respective reactions for different inputs
        return option1
    elif choice1 == 2:
        print ("You have selected", option2)
        return option2
    elif choice1 == 3:
        print ("You have selected", option3)
        return option3
    elif choice1 == 4:
        print ("You have selected", option4)
        return option4
    else:
        return None
    
"""
Type contract: This function takes in 3 string inputs smoothie_type, smoothie_size, topping and return a float cost as result
It assumes global variables are already defined and tester call the function with appropriate parameters accordingly
Example1
>>> calculate_subtotal(SMOOTHIE1_NAME, SIZE4_NAME, TOPPING4_NAME)
105.99
Example2
>>> calculate_subtotal(SMOOTHIE2_NAME, SIZE3_NAME, TOPPING2_NAME)
9.49
Example3
>>> calculate_subtotal(SMOOTHIE2_NAME, SIZE2_NAME, TOPPING1_NAME)
6.49
"""
    
    
def calculate_subtotal(smoothie_type, smoothie_size, topping):
    result = 0.00 #set variable for calculating subtotal
    if SMOOTHIE1_NAME == smoothie_type: #the long code below is for all possible combinations for smoothie name, size and toppings.
        result += 4.99
        if SIZE1_NAME == smoothie_size:
            result -= 2
            if TOPPING1_NAME == topping:
                return result
                print (result)
            else:
                result += 1
                return result
                print (result)
        if SIZE2_NAME == smoothie_size:
            if TOPPING1_NAME == topping:
                return result
                print (result)
            else:
                result += 1
                return result
                print (result)
        if SIZE3_NAME == smoothie_size:
            result += 2
            if TOPPING1_NAME == topping:
                return result
                print (result)
            else:
                result += 1
                return result
                print (result)
        if SIZE4_NAME == smoothie_size:
            result += 100
            if TOPPING1_NAME == topping:
                return result
                print (result)
            else:
                result += 1
                return result
                print (result)
    elif SMOOTHIE2_NAME == smoothie_type:
        result += 6.49
        if SIZE1_NAME == smoothie_size:
            result -= 2
            if TOPPING1_NAME == topping:
                return result
                print (result)
            else:
                result += 1
                return result
                print (result)
        if SIZE2_NAME == smoothie_size:
            if TOPPING1_NAME == topping:
                return result
                print (result)
            else:
                result += 1
                return result
                print (result)
        if SIZE3_NAME == smoothie_size:
            result += 2
            if TOPPING1_NAME == topping:
                return result
                print (result)
            else:
                result += 1
                return result
                print (result)
        if SIZE4_NAME == smoothie_size:
            result += 100
            if TOPPING1_NAME == topping:
                return result
                print (result)
            else:
                result += 1
                return result
                print (result)
    elif SMOOTHIE3_NAME == smoothie_type:
        result += 0.99
        if SIZE1_NAME == smoothie_size:
            result -= 2
            if TOPPING1_NAME == topping:
                return result
                print (result)
            else:
                result += 1
                return result
                print (result)
        if SIZE2_NAME == smoothie_size:
            if TOPPING1_NAME == topping:
                return result
                print (result)
            else:
                result += 1
                return result
                print (result)
        if SIZE3_NAME == smoothie_size:
            result += 2
            if TOPPING1_NAME == topping:
                return result
                print (result)
            else:
                result += 1
                return result
                print (result)
        if SIZE4_NAME == smoothie_size:
            result += 100
            if TOPPING1_NAME == topping:
                return result
                print (result)
            else:
                result += 1
                return result
                print (result)
    else:
        result += 9.99
        if SIZE1_NAME == smoothie_size:
            result -= 2
            if TOPPING1_NAME == topping:
                return result
                print (result)
            else:
                result += 1
                return result
                print (result)
        if SIZE2_NAME == smoothie_size:
            if TOPPING1_NAME == topping:
                return result
                print (result)
            else:
                result += 1
                return result
                print (result)
        if SIZE3_NAME == smoothie_size:
            result += 2
            if TOPPING1_NAME == topping:
                return result
                print (result)
            else:
                result += 1
                return result
                print (result)
        if SIZE4_NAME == smoothie_size:
            result += 100
            if TOPPING1_NAME == topping:
                return result
                print (result)
            else:
                result += 1
                return result
                print (result)

"""
Type contract: this function takes a float subtotal and 3 strings for smoothie name, size and topping options. It outputs receipt with words and 4 floats each for subtotal cost, GST, QST and total.
WARNING! It must be used after command line calling subtotal = calculate_subtotal(...) otherwise can't be used alone! I followed the example!
Example 1
>>> subtotal = calculate_subtotal(SMOOTHIE4_NAME, SIZE4_NAME, TOPPING4_NAME)
>>> subtotal
110.99
>>> total = print_receipt(subtotal, SMOOTHIE1_NAME, SIZE4_NAME, TOPPING4_NAME)
You ordered a galactic Pineapple Banana smoothie with shredded coconut
Smoothie cost:
GST:    5.55
QST:    11.07
Total:  127.61
>>> total
127.61
Example 2 (THE PDF GIVEN EXAMPLE STRESSES THE NEED TO COMMANDLINE ENTER A SUBTOTAL VALUE FIRST! IF YOU GOT AN ERROR THAT"S CUZ YOU DIDN"T ASSIGN SUBTOTAL VALUE!)
>>> subtotal = 110.99
>>> total = print_receipt(subtotal, SMOOTHIE1_NAME, SIZE4_NAME, TOPPING4_NAME)
You ordered a galactic Pineapple Banana smoothie with shredded coconut
Smoothie cost: $ 110.99
GST: $ 5.3
QST: $ 10.6
total: $ 121.89
Example 3
>>> subtotal = 110.99
>>> total = print_receipt(subtotal, SMOOTHIE1_NAME, SIZE1_NAME, TOPPING1_NAME)
You ordered a small Pineapple Banana smoothie with no topping
Smoothie cost: $ 110.99
GST: $ 0.15
QST: $ 0.3
total: $ 3.44

"""

def print_receipt(subtotal, smoothie_type, smoothie_size, topping):
    print ("You ordered a", smoothie_size, smoothie_type, "smoothie with", topping)
    print ("Smoothie cost: $", subtotal)
    """calculate_subtotal(smoothie_type, smoothie_size, topping)"""
    subtotal1 = calculate_subtotal(smoothie_type, smoothie_size, topping)
    print ("GST: $", round(0.05*calculate_subtotal(smoothie_type, smoothie_size, topping), 3))
    print ("QST: $", round(0.1*calculate_subtotal(smoothie_type, smoothie_size, topping), 2))
    GST = round(0.05*calculate_subtotal(smoothie_type, smoothie_size, topping), 2)
    QST = round(0.1*calculate_subtotal(smoothie_type, smoothie_size, topping), 2)
    print ("total: $", round(subtotal1+GST+QST, 2))

"""
Type contract: It doesn't take any input, it greets and asks questions, promopt input and say there is only onion toffee with calling of post question function. then ask size
and topping, so it takes 3 user input in the process. Then it calls calculate subtotal, print receipt function at the end
ALL FUNCTIONS ARE CALLED WITHIN ORDER() FUNCTION SO NOT CALLED OUTSIDE ANY FUNCTION!
Example1
>>> order()
Welcome to Smooth Smoothies Smoothie Ordering System
Have you tried our new Onion Toffee smoothie?

1)   4.99    Pineapple Banana 
2)   6.49    Almond Basil 
3)   0.99    Purple Surprise 
4)   9.99    Onion Toffee
Your choice (1-4): 1
You have selected Pineapple Banana
Unfortunately, we are out of Pineapple Banana 
You will be served Onion Toffee smoothie.
Which smoothie would you like? 
1)   -2      small 
2)   0   medium 
3)   2   large 
4)   100     galactic
Your choice (1-4): 1
You have selected small
Which topping would you like? 
1)   0   no topping 
2)   1   cinnamon 
3)   1   chocolate shavings 
4)   1   shredded coconut
Your choice (1-4): 1
You have selected no topping
You ordered a small Onion Toffee smoothie with no topping
Smoothie cost: $ 7.99
GST: $ 0.4
QST: $ 0.8
total: $ 9.19

Example2
>>> order()
Welcome to Smooth Smoothies Smoothie Ordering System
Have you tried our new Onion Toffee smoothie?

1)   4.99    Pineapple Banana 
2)   6.49    Almond Basil 
3)   0.99    Purple Surprise 
4)   9.99    Onion Toffee
Your choice (1-4): 2
You have selected Almond Basil
Unfortunately, we are out of Almond Basil 
You will be served Onion Toffee smoothie.
Which smoothie would you like? 
1)   -2      small 
2)   0   medium 
3)   2   large 
4)   100     galactic
Your choice (1-4): 2
You have selected medium
Which topping would you like? 
1)   0   no topping 
2)   1   cinnamon 
3)   1   chocolate shavings 
4)   1   shredded coconut
Your choice (1-4): 3
You have selected chocolate shavings
You ordered a medium Onion Toffee smoothie with chocolate shavings
Smoothie cost: $ 10.99
GST: $ 0.549
QST: $ 1.1
total: $ 12.64

Example3
>>> order()
Welcome to Smooth Smoothies Smoothie Ordering System
Have you tried our new Onion Toffee smoothie?

1)   4.99    Pineapple Banana 
2)   6.49    Almond Basil 
3)   0.99    Purple Surprise 
4)   9.99    Onion Toffee
Your choice (1-4): 3
You have selected Purple Surprise
Unfortunately, we are out of Purple Surprise 
You will be served Onion Toffee smoothie.
Which smoothie would you like? 
1)   -2      small 
2)   0   medium 
3)   2   large 
4)   100     galactic
Your choice (1-4): 1
You have selected small
Which topping would you like? 
1)   0   no topping 
2)   1   cinnamon 
3)   1   chocolate shavings 
4)   1   shredded coconut
Your choice (1-4): 3
You have selected chocolate shavings
You ordered a small Onion Toffee smoothie with chocolate shavings
Smoothie cost: $ 8.99
GST: $ 0.45
QST: $ 0.9
total: $ 10.34

"""

def order():
    print ("Welcome to Smooth Smoothies Smoothie Ordering System\nHave you tried our new Onion Toffee smoothie?")
    name1 = SMOOTHIE1_NAME 
    namecost1 = SMOOTHIE1_COST #give global variables simpiler names
    name2 = SMOOTHIE2_NAME 
    namecost2 = SMOOTHIE2_COST
    name3 = SMOOTHIE3_NAME 
    namecost3 = SMOOTHIE3_COST
    name4 = SMOOTHIE4_NAME 
    namecost4 = SMOOTHIE4_COST
    option1 = SIZE1_NAME 
    cost1 = SIZE1_COST
    option2 = SIZE2_NAME 
    cost2 = SIZE2_COST
    option3 = SIZE3_NAME 
    cost3 = SIZE3_COST
    option4 = SIZE4_NAME 
    cost4 = SIZE4_COST

    choice = 0 #pose questions
    question = "Which smoothie would you like?"
    #pose_question_with_costs(question, option1, cost1, option2, cost2, option3, cost3, option4, cost4)
    print ("\n1)\t", namecost1, "\t", name1, "\n2)\t", namecost2, "\t", name2, "\n3)\t", namecost3, "\t", name3,"\n4)\t", namecost4, "\t", name4)
    userinput = input("Your choice (1-4): ") #take user input
    try: choice = int(userinput)
    except ValueError:
        print("Sorry, that is not a valid option.") #prevent invalid entry
    if choice == 1:
        print ("You have selected", name1) #give respective input to different entries
        #return 1
    elif choice == 2:
        print ("You have selected", name2)
        #return 2
    elif choice == 3:
        print ("You have selected", name3)
        #return 3
    elif choice == 4:
        print ("You have selected", name4)
        #return 4
    else:
        return None
    userinput = choice
    #print (userinput)
    if userinput == 1: #tell user the only option is onion toffee
        print ("Unfortunately, we are out of", name1, "\nYou will be served Onion Toffee smoothie.")
        sizechoice = pose_question_with_costs(question, option1, cost1, option2, cost2, option3, cost3, option4, cost4)
    elif userinput == 2:
        print ("Unfortunately, we are out of", name2, "\nYou will be served Onion Toffee smoothie.")
        sizechoice = pose_question_with_costs(question, option1, cost1, option2, cost2, option3, cost3, option4, cost4)
    elif userinput == 3:
        print ("Unfortunately, we are out of", name3, "\nYou will be served Onion Toffee smoothie.")
        sizechoice = pose_question_with_costs(question, option1, cost1, option2, cost2, option3, cost3, option4, cost4)
    elif userinput == 4:
        print ("You will be served Onion Toffee smoothie.")
        sizechoice = pose_question_with_costs(question, option1, cost1, option2, cost2, option3, cost3, option4, cost4)
    else:
        return None
    print ("Which topping would you like?", "\n1)\t", TOPPING1_COST, "\t", TOPPING1_NAME, "\n2)\t", TOPPING2_COST, "\t", TOPPING2_NAME, "\n3)\t", TOPPING3_COST, "\t", TOPPING3_NAME,"\n4)\t", TOPPING4_COST, "\t", TOPPING4_NAME)
    userinput2 = input("Your choice (1-4): ")
    try: choice2 = int(userinput2) 
    except ValueError:
        print("Sorry, that is not a valid option.") #prevent invalid entry
    if choice2 == 1: #feedback for different size chosen"""
        print ("You have selected", TOPPING1_NAME)
        subtotal = calculate_subtotal(SMOOTHIE4_NAME, sizechoice, TOPPING1_NAME)
        print_receipt(subtotal, SMOOTHIE4_NAME, sizechoice, TOPPING1_NAME)
   
    elif choice2 == 2:
        print ("You have selected", TOPPING2_NAME)
        subtotal = calculate_subtotal(SMOOTHIE4_NAME, sizechoice, TOPPING2_NAME)
        print_receipt(subtotal, SMOOTHIE4_NAME, sizechoice, TOPPING2_NAME)
        
    elif choice2 == 3:
        print ("You have selected", TOPPING3_NAME)
        subtotal = calculate_subtotal(SMOOTHIE4_NAME, sizechoice, TOPPING3_NAME)
        print_receipt(subtotal, SMOOTHIE4_NAME, sizechoice, TOPPING3_NAME)
        
    elif choice2 == 4:
        print ("You have selected", TOPPING4_NAME)
        subtotal = calculate_subtotal(SMOOTHIE4_NAME, sizechoice, TOPPING4_NAME)
        print_receipt(subtotal, SMOOTHIE4_NAME, sizechoice, TOPPING4_NAME)
        
    else:
        return None
    
    
    

