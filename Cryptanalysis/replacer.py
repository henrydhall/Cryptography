import string

def new_replace(text, old_char, new_char):
    new_text = ''
    new_text_list = text.split(old_char)
    new_text = new_char.join(new_text_list)
    return new_text

def replace_letter(text, old_char, new_char):
    new_text = ''
    new_text_list = text.split(old_char)
    new_text = new_char.join(new_text_list)
    return new_text

def replace_multiple(old_text, old_char_list, new_char_list):
    new_text = old_text
    if len(old_char_list) != len(new_char_list):
        raise ValueError('lists not same length.')
    for i in range(0,len(new_char_list)):
        new_text = replace_letter(new_text, old_char_list[i], new_char_list[i])
    return new_text

if __name__ == '__main__':
    #print(new_replace('1234','345','X'))
    print(replace_multiple('123',    ['1','2','3'], 
                                        ['  ','.-','..' ]) )