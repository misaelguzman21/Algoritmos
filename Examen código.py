#Misael Guzmán Gutiérrez
#A01209455
 
roman_numeral = [
    (1000, 'M'),
    (900, 'CM'),
    (500, 'D'),
    (400, 'CD'),
    (100, 'C'),
    (90, 'XC'),
    (50, 'L'),
    (40, 'XL'),
    (10, 'X'),
    (9, 'IX'),
    (5, 'V'),
    (4, 'IV'),
    (1, 'I')]

def get_value(number):

    roman = ''

    while number > 0:
        for i, j in roman_numeral:
            while number >= i:
                roman = roman + j
                number = number - i

    return roman

def main():
    
    print(get_value(23))
    print(get_value(2242))
    print(get_value(2021))
    print(get_value(1751))
    print(get_value(1994))



main()
