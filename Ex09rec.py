# Multiply all the elements in a list
def multiply_list(l):
    if l==[]:
        return 1 
   
    return int(l[0]) * multiply_list(l[1:])

    

# Return the factorial of n
def factorial(n):
    if n==0:
        return 1
    return n * factorial(n-1)



# Count the number of elements in the list l
def count_list(l):
    if l==[]:
        return 0

    return 1 + count_list(l[1:])




# Sum all of the elements in a list
def sum_list(l):
    if l==[]:
        return 0

    return int(l[0]) + sum_list(l[1:])



# Reverse a list without slicing or loops
def reverse(l):
    
    if len(l) <= 1:
        return l  
    else:
        return [l[-1]+reverse(l[:-1])



# Fibonacci returns the nth fibonacci number. The nth fibonacci number is
# defined as fib(n) = fib(n-1) + fib(n-2)
def fibonacci(n):
    
    if n==0:
        return 1 

    if n== 1:
        return 1

    return fib(n-1) + fib(n-2)



# Finds the item i in the list l.... RECURSIVELY
def find(l, i):
    
    if l[0] == i:
        return "%r is in the list" % i

    elif len(l) == 1: 
        return "%r is not in the list" %i

    return find(l[1:], i) 




# Determines if a string is a palindrome
def palindrome(some_string):

    if len(some_string)<=1:
        return "The string is a palindrome" 

    elif some_string[0] != some_string[-1]:
        return "The string is not a palindrome" 

    else:
        return palindrome(some_string[1:-1])



# Given the width and height of a sheet of paper, and the number of times to fold it, return the final dimensions of the sheet as a tuple. Assume that you always fold in half along the longest edge of the sheet.
# NOTE: Assume that you always fold in half along the longest edge of the sheet.


def fold_paper(width, height, folds):
    
    if width==0 or height ==0:
        return (0, 0)

    elif folds==0:
        return (width, height)

    elif float(width)>=float(height):
        return fold_paper(float(width)/2, height, folds-1)

    elif float(height)< float(width):
        return fold_paper(float(height)/2, width, folds-1)



# Count up
# Print all the numbers from 0 to target.
# Use n to keep track of where you're at
# ex, to count from 1 - 100, call count_up(100, 1)
#
# Note: we don't have a test case for this one, so just run this
#       script directly
#
# Note #2: We're printing out the numbers, so this script does not 
#          need to return anything!
def count_up(target, n):
    
    print n
        
    if n+1<= target:
        return count_up(target, n+1)
























