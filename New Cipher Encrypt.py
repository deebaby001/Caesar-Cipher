import string

def caesar(text, shift, alphabets):
    
    def shift_alphabet(alphabet):
        return alphabet[shift:] + alphabet[:shift]
    
    begin_shifted_alphabets = tuple(map(shift_alphabet, alphabets))
    end_alphabet = ''.join(alphabets)
    end_shifted_alphabet = ''.join(begin_shifted_alphabets)
    table = str.maketrans(end_alphabet, end_shifted_alphabet)
    return text.translate(table)
plain_text = "This is Dee Test. Hello World!"
print(caesar(plain_text, 5, [string.ascii_lowercase, string.ascii_uppercase, string.punctuation]))