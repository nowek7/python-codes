class Ceaser:
    # Deszyfrowanie
    @staticmethod
    def decode(aText, aCipher):
        output = ''
        for char in aText:
            code = ord(char)
            if code >= 65 and code <= 90:
                sign = code - aCipher
                if sign < 65:
                    sign += 26
                output += chr(sign)
            elif code >= 97 and code <= 122:
                sign = code - aCipher
                if sign < 97:
                    sign += 26
                output += chr(sign)
        print('{} ----> {}'.format(aText, output))

    # Szyfrowanie
    @staticmethod
    def encode(aText, aCipher):
        output = ''
        for char in aText:
            code = ord(char)
            if code >= 65 and code <= 90:
                sign = code + aCipher
                if sign > 90:
                    sign -= 26
                output += chr(sign)
            elif code >= 97 and code <= 122:
                sign = code + aCipher
                if (sign > 122):
                    sign -= 26
                output += chr(sign)
        print('{} ----> {}'.format(aText, output))
