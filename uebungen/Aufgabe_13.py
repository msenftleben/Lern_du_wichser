def rot13(txt):
    assert type(txt) is str
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYXZ"
    txt_coded = ""
    for letter in txt:
        letter_position = alphabet.find(letter)
        if letter_position >= 0:
            letter = alphabet[(letter_position + 13) % 26]
        txt_coded += letter
    return txt_coded


def test_rot13():
    assert rot13("TEXT") == "GRKG"
    assert rot13("GRKG") == "TEXT"
    assert rot13("HELLO WORLD") == "URYYB JBEYQ"


if __name__ == "__main__":
    test_rot13()
