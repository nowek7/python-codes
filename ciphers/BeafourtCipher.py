class BeafourtMono:
  @staticmethod
  def change(aText, aKey):
    output = ''
    for sign in aText:
      code = ord(sign)
      if code >= 65 and code <= 90:
        sign = (- (code - 65) + aKey) % 26 + 65
        output += chr(sign)
      elif code >= 97 and code <= 122:
        sign = (- (code - 97) + aKey) % 26 + 97
        output += chr(sign)
    print('{} ----> {}'.format(aText, output))

