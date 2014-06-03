from collections import OrderedDict
def romanize(number):
    romanized_number = ''
    list_dict = OrderedDict([[1000, 'M'], [900, 'CM'], [500, 'D'], [400, 'CD'], [100, 'C'], [90, 'XC'], [50, 'L'], [40, 'XL'],
                    [10, 'X'], [9, 'IX'], [5, 'V'], [4, 'IV'], [1, 'I']])
    for key in list_dict:
        print key
        if number - key[0] >= 0:
            number -= key[0]
            romanized_number += key[0]

    if number == 0:
        raise ValueError('can not encode zero')
    if number < 0:
        raise ValueError('can not encode negative number')

    # for lista in list_dict:
    #     while number - lista[1] >0:
    #         number = number - lista[1]
    #         romanized_number += lista[0]
    # return romanized_number
print romanize(345)