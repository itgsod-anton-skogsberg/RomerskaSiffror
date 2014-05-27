def romanize(cleartext):
    output = ''
    numbers = [1000,500,100,50,10,5,1]
    if cleartext == 0:
        raise ValueError('can not encode zero')
    if cleartext < 0:
        raise ValueError('can not encode negative number')

    return output
