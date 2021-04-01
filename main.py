import string

num_roman = 'XXXXX'
values = {
    'M': 1000,
    'D': 500,
    'C': 100,
    'L': 50,
    'X': 10,
    'V': 5,
    'I': 1
}


def roman_to_decimal(roman_number):
    # Obtiene el numero decimal por unidad en una lista

    array_decimals = obtain_array_decimals(roman_number)

    # Obtenemos el numero romano segmentado por partes en una lista

    obtain_result_number(array_decimals)

    #


def obtain_array_decimals(roman_number):
    array_decimals = []

    for i in roman_number:
        array_decimals.append(values.get(i))
    return array_decimals


def obtain_result_number(array_decimals):
    result = 0

    result = result + int(first_mayor(array_decimals))

    result = result + int(second_mayor(array_decimals))

    print(result)


def second_mayor(array_decimals):
    first_number = array_decimals[0]
    second_number = array_decimals[1]
    third_number = array_decimals[2]
    fourth_number = array_decimals[3]
    five_number = array_decimals[4]

    if first_number < second_number:
        return second_number - first_number

    return 0


def first_mayor(array_decimals):
    first_number = array_decimals[0]
    second_number = array_decimals[1]
    third_number = array_decimals[2]
    fourth_number = array_decimals[3]
    five_number = array_decimals[4]

    result = 0

    if first_number >= second_number:

        result = first_number + second_number

        if first_number >= third_number:

            result = result + third_number

            if first_number >= fourth_number:

                result = result + fourth_number

                if first_number > five_number:
                    return

                if first_number == five_number:
                    result = result + five_number

                if first_number < five_number:
                    result = five_number - result

            if first_number < fourth_number:
                result = fourth_number - (first_number + second_number + third_number)

        if first_number < third_number:
            result = third_number - (first_number + second_number)

    return result


if __name__ == '__main__':
    roman_to_decimal(num_roman)
