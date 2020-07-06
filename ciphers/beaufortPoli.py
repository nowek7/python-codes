class beaufortPoli:
  @staticmethod
  def change(key, input_txt):
    output_txt = []
    for pos in range(0, len(input_txt)):
      letter_row = 'A'
      letter_txt = input_txt[pos]
      while letter_txt != key[pos % len(key)]:
        letter_txt = chr((ord(letter_txt)-ord('A')+1) % 26
          + ord('A'))
        letter_row = chr((ord(letter_row)-ord('A')+1) % 26
          + ord('A'))
      output_txt.append(letter_row)
    return ''.join(output_txt)
