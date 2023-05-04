# Import our asssistant
from decrypt_assistant import Decryptinator 

# Other libraries
import random
import morse_translator

morse_list = ['  ','.-','..','--','-.',' .','. ', '- ', ' -']
number_list = ['1','2','3','4','5','6','7','8','9']

# Get our cipher text put in
my_decryptor = Decryptinator(f'4276874682762636\
2477686878657561721564765746574314268241765673146377115937868163\
6738641695661941928869424636687528287715171474174637681636619282\
78737414212818178136872')

# I just brute forced this sucker
random.shuffle(number_list)
while True:
    random.shuffle(number_list)
    try:
        print( morse_translator.decrypt( my_decryptor.try_replace( number_list, morse_list ) ) )
        print(number_list)
    except:
        pass

# Running for at least 30 seconds should have given at least one output of...
print(['9', '4', '8', '3', '5', '6', '7', '2', '1'])
print('WE HAVE A RARE SHIPMENT OF PAPPY VAN WINKLE TO DISTRIBUTE MEET AT THE WAREHOUSE ON CANAL STREET TUESDAY MIDNIGHT')

# So our key is 948356721, and we need to go to the warehouse on canal street to bust them
# I knew brute force would work because there's so many combinations that throw out garbage
# that the morse translator would throw an error for, and figured I could sift through everything 
# else until I could narrow the keys down, or find the full answer.