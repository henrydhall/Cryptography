# Henry Hall

from frequency_report import FrequencyAnalyzer
import replacer
import morse_translator
import random
from playfair_decrypter import playfield_brute_force

class Decryptinator:
    """My useful friend for helping break codes."""
    def __init__(self, cipher_text_):
        self.cipher_text = cipher_text_
        self.frequency_analysis = FrequencyAnalyzer(self.cipher_text)
    
    def see_frequency(self):
        self.frequency_analysis.display_frequency_chart()

    def try_replace(self, crypt, decrypt):
        return replacer.replace_multiple(self.cipher_text,crypt,decrypt)
    
    def brute_force(self, crypt, decrypt, n = 10000, translator = None):
        # TODO: add option for expected words
        # TODO: add option for known or expected keys
        # TODO: add option for keys that are known to not be valid, unexpected keys
        i = 0
        rand_crypt = crypt
        random.shuffle(rand_crypt)
        if translator == None:
            while i < n:
                random.shuffle(rand_crypt)
                i = i + 1
                try:
                    print( self.try_replace(crypt,decrypt) )
                    print( rand_crypt )
                except:
                    pass
        else:
            while i < n:
                random.shuffle(number_list)
                i = i + 1
                try:
                    print( translator( my_decryptor.try_replace( number_list, morse_list ) ) )
                    print(number_list)
                except:
                    pass

my_decryptor = Decryptinator(f'4276874682762636\
2477686878657561721564765746574314268241765673146377115937868163\
6738641695661941928869424636687528287715171474174637681636619282\
78737414212818178136872')

if __name__ == '__main__':
    pass
    #morse_list = ['  ','.-','..','--','-.',' .','. ', '- ', ' -']
    #number_list = ['1','2','3','4','5','6','7','8','9']
    #my_decryptor.brute_force(number_list,morse_list, 1000000,morse_translator.decrypt)
    