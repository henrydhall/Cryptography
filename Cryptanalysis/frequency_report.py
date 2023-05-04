# Frequency Analysis Tool

import string
from matplotlib import markers, pyplot as plt, use

class FrequencyAnalyzer:
    """
    Class to help me do frequency analysis of texts.
    """
    def __init__(self):
        self.cipher_text = string
        self.alphabet = set()
        self.frequencies = dict()

    def __init__( self, cipher_text_ ): 
        self.cipher_text = cipher_text_
        self.alphabet = self.generate_alphabet(self.cipher_text)
        self.frequencies = self.generate_frequencies()

    def get_cipher(self):
        return self.cipher_text

    def generate_alphabet(self, text):
        new_alphabet = set()
        for letter in text:
            new_alphabet.add(letter)
        return new_alphabet

    def get_alphabet(self ):
        return self.alphabet

    def get_frequencies(self):
        return self.frequencies

    def generate_frequencies(self):
        new_frequencies = dict()
        letter_count = 0
        for letter in self.alphabet:
            new_frequencies[letter] = self.cipher_text.count(letter)
        return new_frequencies

    def display_frequency_chart(self):
        frequency_dict = self.frequencies
        letters = list(frequency_dict.keys() )
        letters.sort()
        frequencies = [ frequency_dict[letter] for letter in letters ]
        plt.bar(letters, frequencies)
        plt.title('Letter Frequencies')
        plt.ylabel('# of occurences')
        plt.show()

if __name__ == '__main__':
    my_ciph = FrequencyAnalyzer(f'4276874682762636\
2477686878657561\
7215647657465743\
1426824176567314\
6377115937868163\
6738641695661941\
9288694246366875\
2828771517147417\
4637681636619282\
7873741421281817\
8136872')
    print( my_ciph.display_frequency_chart() )