import string
def caesar(text, shift, alphabets):            #Defining caesar
    
    def shift_alphabet(alphabet):                 #Defining the shifted alphabet
        return alphabet[shift:] + alphabet[:shift]
    
    begin_shifted_alphabets = tuple(map(shift_alphabet, alphabets))       #Use tuple to map the definitions then use joins
    end_alphabet = ''.join(alphabets)
    end_shifted_alphabet = ''.join(begin_shifted_alphabets)
    table = str.maketrans(end_alphabet, end_shifted_alphabet)  #indicating the translation table
    return text.translate(table)

plain_text = "Ymnx nx Ijj Yjxy= Mjqqt Btwqi&" #Converting or deciphering the message to the original string; performing shift
shift = 26 - 5
shift %= 26
print(caesar(plain_text, 21, [string.ascii_lowercase, string.ascii_uppercase, string.punctuation]))
