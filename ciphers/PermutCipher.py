import string

horizontalRule = ['-' * 105]
primaryAlphabet = list(string.ascii_lowercase)
cipherAlphabet = []
dictionary = {}


def setEncodedAlphapbet(aCipher):
    for sign in aCipher.replace(' ', ''):
        if ord(sign) >= 97 and ord(sign) <= 122:
            if sign not in cipherAlphabet:
                cipherAlphabet.append(sign)
        else:
            print('Cipher has unacceptable sign. Check ASCII table!')

    for sign in ''.join(primaryAlphabet):
        if sign not in cipherAlphabet:
            cipherAlphabet.append(sign)


def printAlphabet():
    """
    Print primary alphabet and encoded alphabet in table.
    """
    print(' '.join(horizontalRule))
    print('| ' + ' | '.join(primaryAlphabet) + ' |')
    print(' '.join(horizontalRule))
    print('| ' + ' | '.join(cipherAlphabet) + ' |')
    print(' '.join(horizontalRule))
    print()
    print()


def decode(aText):
    decodedText = []
    for char in ''.join(aText):
        index = cipherAlphabet.index(char)
        decodedText.append(primaryAlphabet[index])

    print('Rozszyfrowany tekst:')
    print(aText + ' ---> ' + ''.join(decodedText))


def encode(aText):
    encodedText = []
    for char in ''.join(aText):
        index = primaryAlphabet.index(char)
        encodedText.append(cipherAlphabet[index])

    print('Zaszyfrowany tekst:')
    print(aText + ' ---> ' + ''.join(encodedText))


# Main program
cipher = str(input('Wpisz szyfr: ')).lower()
setEncodedAlphapbet(cipher)
printAlphabet()

text = str(input('Wpisz słowe do zaszyfrowanie / rozszyfrowania: '))
choose = int(input('\n Zaszyfrować : 1 \n Rozszyfować : 2 \n Wybór -> '))

if choose == 1:
    encode(text)
elif choose == 2:
    decode(text)
else:
    print('Error! Mamy tylko dwie opcje :-(')
