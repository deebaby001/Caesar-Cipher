#Purpose: Overall, in the first part of the code this is basic encryption 
# which shifts each letter of a message by a 
#given number of positions down a the standard alphabet. 
# Then in the later part of the code, I am handling the decryption of the coded message back to the original message.

import string 

def caesar(text, shift, alphabets):          #Defining caesar function that uses three arguments: text, shift and alphabets
    
    def shift_alphabet(alphabet):               #Defining the function shifted alphabet using one argument
        return alphabet[shift:] + alphabet[:shift]    #Returning the new string that is the result of shifting the letters in alphabet by shift position
    
    begin_shifted_alphabets = tuple(map(shift_alphabet, alphabets))    #A new tuple named begin_shifted_alphabets by using the function, shift_alphabet, for each element in alphabets 
    end_alphabet = ''.join(alphabets)     #New string created called end__shifted_alphabet by joining all strings in begin_shifted_alphabets
    end_shifted_alphabet = ''.join(begin_shifted_alphabets)
    table = str.maketrans(end_alphabet, end_shifted_alphabet)    #Defines a translation table using the str.maketrans method, this maps each character in end_alphabet to corresponding character in end_shifted_alphabet
    return text.translate(table)                                #Returns a new string that resulted from using the translation table to text


plain_text = "Ymnx nx Ijj Yjxy= Mjqqt Btwqi&" #Converting or deciphering the message to the original string; performing shift
shift = 26 - 5
shift %= 26                                   
print(caesar(plain_text, 21, [string.ascii_lowercase, string.ascii_uppercase, string.punctuation]))
