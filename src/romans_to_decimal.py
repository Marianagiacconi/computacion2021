def roman_to_decimal(roman_number):
    print('vamos a ver que pasa con ' + roman_number)
    result = 0
    for roman_letter in roman_number:
        print('veamos que tiene el roman_letter' + roman_letter)
        if roman_letter == 'I':
            print('vamos a sumar 1')
            result = result + 1
        if roman_letter == 'V':
            print('vamos a sumar 5')
            result = result + 5
    return result