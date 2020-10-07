#Ken Li 260823059

"""
Type contract: This function takes 9 ints and calculates and return checksum of a 10 digit ISBN as string                                                                                                     
example1
>>>calculate_isbn_checksum_by_digits(8, 7, 1, 1, 0, 7, 5, 5, 9)
7
example2
>>> calculate_isbn_checksum_by_digits(2, 8, 1, 5, 0, 7, 6, 5, 9)
4
example3
>>> calculate_isbn_checksum_by_digits(1, 2, 3, 4, 5, 7, 6, 5, 9)
7

"""
def calculate_isbn_checksum_by_digits(d1, d2, d3, d4, d5, d6, d7, d8, d9):
    result = (d1 + 2*d2 + 3*d3 + 4*d4 + 5*d5 + 6* d6 + 7* d7 + 8* d8 + 9* d9)%11 #use formula indicated by PDF
    return result

"""
Type contract: This function takes an int input of 9 digit integer for 9 leftmost digits of ISBN, calculates and returns checksum as string
example1
>>> calculate_isbn_checksum(871107559)
7
example2
>>> calculate_isbn_checksum(567897559)
5
example3
>>> calculate_isbn_checksum(567823456)
0

"""
def calculate_isbn_checksum(isbn): #use // to take down each integer at a time to break a long entry
    d9 = isbn % 10
    isbn //= 10
    d8 = isbn % 10
    isbn //= 10
    d7 = isbn % 10
    isbn //= 10
    d6 = isbn % 10
    isbn //= 10
    d5 = isbn % 10
    isbn //= 10
    d4 = isbn % 10
    isbn //= 10
    d3 = isbn % 10
    isbn //= 10
    d2 = isbn % 10
    isbn //= 10
    d1 = isbn % 10
    isbn //= 10
    result1 = (d1 + 2*d2 + 3*d3 + 4*d4 + 5*d5 + 6* d6 + 7* d7 + 8* d8 + 9* d9)%11 #use same formula
    return result1

"""
It takes a int input for 9 left digits of isbn and a string checksum and check if isbn valid return boolean true otherwise false
example1
>>> is_isbn(871107559, "4")
False
example2
>>> is_isbn(567897559, "5")
True
example3
>>> is_isbn(513824559, "2")
False
"""
    
def is_isbn(isbn, checksum):
    compare = calculate_isbn_checksum(isbn) #compare isbn calculation result with the input checksum
    numberchecksum = int(checksum)
    if compare == numberchecksum:
        return True
    else: return False

"""
it takes 6 int inputs as dimensions for box and book, and return boolean true and false if boox can fit in box
It can be rotated
example1
>>> book_fits_in_box(15, 2, 2, 2, 15, 2)
True
example2
>>> book_fits_in_box(10, 2, 2, 4, 20, 2)
False
example3
>>> book_fits_in_box(100, 20, 20, 4, 20, 2)
True
"""

def book_fits_in_box(box_w, box_d, box_h, book_w, book_d, book_h):
    if (book_w <= box_w and box_d and box_h) and (book_d <= box_w and box_d and box_h) and (book_h <= box_w and box_d and box_h):
        return True
    else: return False
    
"""
It takes 3 int inputs as book dimension and output a string indicating box size that can fit, if not return empty string
example1
>>> get_smallest_box_for_book(12, 12, 2)
'medium'
example2
>>> get_smallest_box_for_book(20, 22, 3)
''
example3
>>> get_smallest_box_for_book(1, 1, 1)
'small'
"""

def get_smallest_box_for_book(book_w, book_d, book_h): #use previous function and given box dimension to compare
    if book_fits_in_box(10, 10, 2, book_w, book_d, book_h) is True:
        print ("'small'")
    elif book_fits_in_box(15, 15, 3, book_w, book_d, book_h) is True:
        print ("'medium'")
    elif book_fits_in_box(20, 20, 4, book_w, book_d, book_h) is True:
        print ("'large'")
    else: return ''

"""
It takes 6 int inputs for box and book's dimensions and return an int output of max number of books that can fit in given box dimensionb
example1
>>> get_num_books_for_box(10, 5, 5, 5, 5, 2)
4
example2
>>> get_num_books_for_box(10, 10, 10, 5, 5, 2)
20
example3
>>> get_num_books_for_box(10, 10, 10, 15, 15, 12)
can't get in box
"""

def get_num_books_for_box(box_w, box_d, box_h, book_w, book_d, book_h): #First make sure book dimensions < box dimensions. Since box can rotate, do num = w * d * h
    if (book_w <= box_w and book_d <= box_d and book_h <= box_h)is True:
        w = int(box_w/book_w)
        d = int(box_d/book_d)
        h = int(box_h/book_h)
        num = w * d * h
        print (num)
    else: print ("can't get in box")
    
"""
It doesn't take any input, it greet user and display option, prompt user input for int choice and call different functions and return their outputs
example1
>>> main()
Welcome to the shipment calculation system.
1) Check ISBN 
2) Check box/book size
3) Get smallest box size for book
4) Get num equally-sized books per box
Enter choice (1-4):1
Enter ISBN: 110101011
Enter checksum: 1
ISBN is not valid (checksum did not match).
example2
>>> main()
Welcome to the shipment calculation system.
1) Check ISBN 
2) Check box/book size
3) Get smallest box size for book
4) Get num equally-sized books per box
Enter choice (1-4):2
Enter 6 values strictly in order of box_w box_d box_h book_w book_d book_h, NO COMMA: 30 20 10 10 10 10
True
example3
>>> main()
Welcome to the shipment calculation system.
1) Check ISBN 
2) Check box/book size
3) Get smallest box size for book
4) Get num equally-sized books per box
Enter choice (1-4):3
Enter 3 values strictly in order of book_w book_d book_h, NO COMMA: 5 5 5
'small'


"""
    
def main():
    print ("Welcome to the shipment calculation system.\n1) Check ISBN ")
    print ("2) Check box/book size")
    print ("3) Get smallest box size for book")
    print ("4) Get num equally-sized books per box")

    entry = int(input("Enter choice (1-4):"))
    if entry == 1:
        isbn = int(input("Enter ISBN: "))
        """match = calculate_isbn_checksum(isbn)
        print (match)"""
        checksum = int(input("Enter checksum: "))
        if is_isbn(isbn, checksum) is True:
            print("ISBN is valid.")
        else: print("ISBN is not valid (checksum did not match).")
    
    elif entry == 2:
        box_w, box_d, box_h, book_w, book_d, book_h = map(int,input("Enter 6 values strictly in order of box_w box_d box_h book_w book_d book_h, NO COMMA: ").split())
        print(book_fits_in_box(box_w, box_d, box_h, book_w, book_d, book_h))        
    
    elif entry == 3:
        book_w, book_d, book_h = map(int,input("Enter 3 values strictly in order of book_w book_d book_h, NO COMMA: ").split())
        get_smallest_box_for_book(book_w, book_d, book_h)
        
    elif entry == 4:
        box_w, box_d, box_h, book_w, book_d, book_h = map(int,input("Enter 6 values strictly in order of box_w box_d box_h book_w book_d book_h, NO COMMA: ").split())
        get_num_books_for_box(box_w, box_d, box_h, book_w, book_d, book_h)
        
    else: return ''
        
            
        
        
