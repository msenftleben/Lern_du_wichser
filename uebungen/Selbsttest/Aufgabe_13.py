def rot13(txt):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    coded_txt = ""
    for letter in txt:
        letter_position = alphabet.find(letter)
        if letter_position > 0:
            letter = alphabet[(letter_position + 13) % 26]
        coded_txt += letter
    return coded_txt
