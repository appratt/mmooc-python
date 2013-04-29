# This program takes a string as an argument and tests to see if it is a palindrome. Capitalization does not matter.

def is_palindrome(string):
    letter_list = string.lower() #make string lowercase
    letter_list = list(letter_list) #conver the string to a list
    letter_list_length = len(letter_list)

    palindrome = 'TRUE' #The WHILE loop below assumes that as long as the conditions are met (first and last letter are the same), it's a palindrome. The loop breaks letters off the ends of the strong and tests the next letters, then repeats while those next letters are the same. The loop breaks when the letters are no longer the same, returning palindrome = 'FALSE'

    first_letter = letter_list[0]   
    last_letter = letter_list[-1]


    while first_letter==last_letter:
        del letter_list[0] #remove the first letter
        del letter_list[-1] #remove the last letter
        
        letter_list_length = len(letter_list) #measure the length of the new string and store it
        #If the length of the string gets down to 1, then there's no point in popping off more letters: it's a palindrome.
        if letter_list_length > 1:
            first_letter = letter_list[0]   
            last_letter = letter_list[-1]
            print letter_list_length
            print first_letter
            print last_letter
        else:
            palindrome = 'TRUE'
            break
    else:
        palindrome = 'FALSE'


    return "Is it a palindrome? (TRUE/FALSE)", palindrome, "Number of characters remaining after all the outside characters were tested for equivalence: ",letter_list_length



print is_palindrome('ana')