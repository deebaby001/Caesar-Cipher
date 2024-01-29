import string

def caesar(text, shift, alphabets):                #Defining caesar
    
    def shift_alphabet(alphabet):                       #Defining shifted alphabet 
        return alphabet[shift:] + alphabet[:shift]
    
    begin_shifted_alphabets = tuple(map(shift_alphabet, alphabets))             #Use tuple to map definitions then use joins
    end_alphabet = ''.join(alphabets)
    end_shifted_alphabet = ''.join(begin_shifted_alphabets)
    table = str.maketrans(end_alphabet, end_shifted_alphabet)                      #Indicating the translation table
    return text.translate(table)
plain_text = "This is Dee Test. Hello World!"
print(caesar(plain_text, 5, [string.ascii_lowercase, string.ascii_uppercase, string.punctuation]))