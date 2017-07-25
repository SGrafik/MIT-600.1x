def convert_to_mandarin(us_num):
    '''
    us_num, a string representing a US number 0 to 99
    returns the string mandarin representation of us_num
    '''

    trans = {'0':'ling', '1':'yi', '2':'er', '3':'san', '4': 'si',
          '5':'wu', '6':'liu', '7':'qi', '8':'ba', '9':'jiu', '10': 'shi'}

    check = int(us_num)

    if check <= 10:
        if check == 10:
            return 'shi'
        else:
            translation = [trans[i] for i in us_num]

    elif 11 <= check <= 19:
        translation = ['shi', trans[us_num[1]]]

    elif 20 <= check <= 99:
        if us_num[1] == '0':
            translation =  trans[us_num[0]] + ' shi'
            return translation
        else:
            translation = [trans[i] for i in us_num]
        return ' shi '.join(translation)

    return ' '.join(translation)

print(convert_to_mandarin('30'))
