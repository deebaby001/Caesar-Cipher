import string
def caesar(text, shift, alphabets):
    
    def shift_alphabet(alphabet):
        return alphabet[shift:] + alphabet[:shift]
    
    begin_shifted_alphabets = tuple(map(shift_alphabet, alphabets))
    end_alphabet = ''.join(alphabets)
    end_shifted_alphabet = ''.join(begin_shifted_alphabets)
    table = str.maketrans(end_alphabet, end_shifted_alphabet)
    return text.translate(table)

plain_text = "Ymnx nx Ijj Yjxy= Mjqqt Btwqi&"
shift = 26 - 5
shift %= 26
print(caesar(plain_text, 21, [string.ascii_lowercase, string.ascii_uppercase, string.punctuation]))
