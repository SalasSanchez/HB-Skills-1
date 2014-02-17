# Things you should be able to do.

# Write a function that takes a list and returns a new list with only the odd numbers.
def all_odd(some_list):

    odds = []

    for n in range(len(some_list)):
        if (some_list[n])%2!=0:
            odds.append(some_list[n])

    return odds

#This is the same but simpler:

def all_odd(some_list):

    odds = []

    for n in some_list:
        if n%2!=0:
            odds.append(n)

    return odds


# Write a function that takes a list and returns a new list with only the even numbers.
def all_even(some_list):
    evens = []

    for n in some_list:
        if n%2==0:
            evens.append(n)

    return evens



# Write a function that takes a list of strings and a new list with all strings of length 4 or greater.
def long_words(word_list):
    
    longs = []
    for word in word_list:
        if len(word)>= 4:
            longs.append(word)

    return longs


# Write a function that finds the smallest element in a list of integers and returns it.
def smallest(some_list):
    
    smallest = some_list[0]
    
    for n in range(len(some_list)):
        if some_list[n] < smallest:
            smallest = some_list[n]
         
    
    return smallest 

#This is much simpler:

def smallest(some_list):
    
    smallest = some_list[0]
    
    for n in some_list:
        if n < smallest:
            smallest = n
         
    
    return smallest 


# Write a function that finds the largest element in a list of integers and returns it.
def largest(some_list):
    
    largest = some_list[0]

    for n in some_list:
        if n > largest:
            largest = n

    return largest



# Write a function that takes a list of numbers and returns a new list of all those numbers divided by two.
def halvesies(some_list):
    
    halves = []

    for n in some_list:
        halves.append(n/2)

    return halves


# Write a function that takes a list of words and returns a list of all the lengths of those words.
def word_lengths(word_list):

    lengths = []

    for word in word_list:
        lengths.append(len(word))

    return lengths



# Write a function (using iteration) that sums all the numbers in a list.
def sum_numbers(numbers):
    
    total = 0
    for n in numbers:
        total += n

    return total 



# Write a function that multiplies all the numbers in a list together.
def mult_numbers(numbers):
    
    total = 1
    for n in numbers:
        total *= n

    return numbers 



# Write a function that joins all the strings in a list together (without using the join method) and returns a single string.
def join_strings(string_list):
    
    one_string = ""

    for string in string_list:
        one_string += string

    return one_string 



# Write a function that takes a list of integers and returns the average (without using the avg method)
def average(numbers):
    
    total = 0
    for n in numbers:
        total += n


    return total/len(numbers)