# key = [int(x) for x in input("Klucz (a, b): ").split()]
# text = str(input('Wpisz słowe do zaszyfrowanie / rozszyfrowania: '))
# choose = int(input('\n Zaszyfrować : 1 \n Rozszyfować : 2 \n Wybór -> '))

def inverseModulo(aNumber):
    for i in range(1,26):
        output = (aNumber * i) % 26
        if output == 1:
            return i
    else:
        raise ValueError('Nie istnieje liczba odwrotna modulo 26 liczby {}', aNumber)

class Affine:
    @staticmethod
    def decode(aText, aKey):
        inverseMod = inverseModulo(aKey[0])
        result = ''
        for char in aText:
            code = ord(char)
            if code >= 65 and code <= 90:
                sign = (aKey[0] * (code - 65 - aKey[1])) % 26 + 65
                result += chr(sign)
            elif code >= 97 and code <= 122:
                sign = (aKey[0] * (code - 97 - aKey[1])) % 26 + 97
                result += chr(sign)
        print('{} ----> {}'.format(aText, result))

    @staticmethod
    def encode(aText, aKey):
        result = ''
        for char in aText:
            code = ord(char)
            if code >= 65 and code <= 90:
                sign = (aKey[0] * (code - 65) + aKey[1]) % 26
                result += chr(sign + 65)
            elif code >= 97 and code <= 122:
                sign = (aKey[0] * (code - 97) + aKey[1]) % 26
                result += chr(sign + 97)
        print('{} ----> {}'.format(aText, result))



# def gauss(A):
#     n = len(A)

#     for i in range(0, n):
#         # Search for maximum in this column
#         maxEl = abs(A[i][i])
#         maxRow = i
#         for k in range(i+1, n):
#             if abs(A[k][i]) > maxEl:
#                 maxEl = abs(A[k][i])
#                 maxRow = k

#         # Swap maximum row with current row (column by column)
#         for k in range(i, n+1):
#             tmp = A[maxRow][k]
#             A[maxRow][k] = A[i][k]
#             A[i][k] = tmp

#         # Make all rows below this one 0 in current column
#         for k in range(i+1, n):
#             c = -A[k][i]/A[i][i]
#             for j in range(i, n+1):
#                 if i == j:
#                     A[k][j] = 0
#                 else:
#                     A[k][j] += c * A[i][j]

#     # Solve equation Ax=b for an upper triangular matrix A
#     x = [0 for i in range(n)]
#     for i in range(n-1, -1, -1):
#         x[i] = A[i][n]/A[i][i]
#         for k in range(i-1, -1, -1):
#             A[k][n] -= A[k][i] * x[i]
#     return x

# def crack(aText, aCrack):
#     matrix = [[ord(aCrack[0]), 1, ord(aText)], [ord(aCrack[1]), 1, ord(aText)]]
#     key = gauss(matrix)
#     decode(aText, key)


# if choose == 1:
#     encode(text, key)
# elif choose == 2:
#     decode(text, key)
# else:
#     print('Błąd! Mamy tylko dwie opcje :-(')
