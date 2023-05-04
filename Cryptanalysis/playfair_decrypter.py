import string
import random

def play_field_builder(key):
    key = key.upper() + string.ascii_uppercase
    square_key = '\n'
    for letter in key:
        if letter not in square_key and letter != ' ' and letter != 'J' and letter != '\n':
            square_key = square_key + letter
        if len(square_key ) % 6  == 0:
            square_key = square_key + '\n'
    return square_key

def special_playfield( key, text ):
    plain_text = ''
    i = 0
    while i < len(text)-1:
        first = text[i]
        second = text[i+1]
        i = i + 2
        position_first = key.find(first)
        position_second = key.find(second)
        #Same row checks
        if (position_first < 5 and position_second < 5):
            position_first = position_first + 5
            position_second = position_second + 5
        elif(position_first >= 5 and position_first < 10 and position_second >= 5 and position_second < 10 ):
            position_first = position_first + 5
            position_second = position_second + 5
        elif(position_first >= 10 and position_first < 15 and position_second >= 10 and position_second < 15 ):
            position_first = position_first + 5
            position_second = position_second + 5
        elif(position_first >= 15 and position_first < 20 and position_second >= 15 and position_second < 20 ):
            position_first = position_first + 5
            position_second = position_second + 5
        elif(position_first >= 20 and position_first < 25 and position_second >= 20 and position_second < 25 ):
            position_first = position_first + 5
            position_second = position_second + 5
        #Same column checks
        elif(position_first % 5 == position_second % 5):
            if position_first % 5 != 0:
                position_first = position_first - 1
            else:
                position_first = position_first + 4
            if position_second % 5 != 0:
                position_second = position_second - 1
            else:
                position_second = position_second + 4
        #For rectangle
        else:
            position_first = position_first - 5
            position_second = position_second - 5
        
        plain_text = plain_text + key[position_first % 25] + key[position_second % 25]
    return plain_text

#This isn't working...

def playfield_brute_force(key, cipher_text): 
    potential_plain = special_playfield(key,cipher_text)

    if 'ESCAPE' in potential_plain or 'TUCSON' in potential_plain:
        return potential_plain
    elif 'BRENDA' in potential_plain or 'LAUNDER' in potential_plain:
        return potential_plain
    elif 'ARIZONA' in potential_plain:
        return potential_plain
    elif 'JAIL' in potential_plain:
        return potential_plain
    else:
        raise ValueError('nope')
    
def run_brute_force():
    cipher = 'TBBYBHMNXWVUGXOPVUGCPUTVOIYRBTTVHGBFVZVDYCYSBUUZLOWS'
    scramble_alphabet = [letter for letter in 'ABCDEFGHIKLMNOPQRSTUVWXYZ' ]
    alphabet = 'ABCDEFGHIKLMNOPQRSTUVWXYZ'
    cipher = 'TBBYBHMNXWVUGXOPVUGCPUTVOIYRBTTVHGBFVZVDYCYSBUUZLOWS'

    random.shuffle(scramble_alphabet)
    i = 0
    while True:
        i = i + 1
        random.shuffle(scramble_alphabet)
        try:
            print( playfield_brute_force( ''.join(scramble_alphabet), cipher  ) )
            print(''.join(scramble_alphabet) )
        except:
            pass

def one_case():
    alphabet = 'ABCDEFGHIKLMNOPQRSTUVWXYZ'
    text = 'AFCGXY'
    print( special_playfield(alphabet, text) )

if __name__ == '__main__':
    #run_brute_force()
    cipher = 'TBBYBHMNXWVUGXOPVUGCPUTVOIYRBTTVHGBFVZVDYCYSBUUZLOWS'
    key = play_field_builder('tusconarizona')
    key = ''.join( key.strip().split() ) 
    print(key)
    print(special_playfield(key, cipher) )