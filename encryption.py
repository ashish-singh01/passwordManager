def encrypt(password):

    newPass = ''

    print('Encryption ON')
    
    for letter in password:
        value = ord(letter)
        print(value)
        if value <= 96:
            value+=30

        elif value > 96:
            value = 32+(127-value-1)

        newPass += chr(value)
        print(value)

    return newPass

    print('Encryption OFF')

def decrypt(password):

    print('Decryption ON')
    print(password)
    newPass = ''
    
    for letter in password:
        value = ord(letter)
        print(value)
        if value >= 62:
            value = value - 30
        elif value < 62:
            value = 127 - (value-32) -1
        print (value)
        newPass += chr(value)

    return newPass

    print('Decryption OFF')

