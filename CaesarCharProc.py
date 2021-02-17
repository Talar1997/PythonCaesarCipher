class CaesarCharProc:
    alphabet = None
    alphabetLength = None
    offset = None

    def __init__(self, alphabet, offset) -> None:
        self.alphabet = alphabet
        self.alphabetLength = len(self.alphabet)
        self.offset = int(offset)

    def process(self, char) -> str:
        char_index = self.alphabet.index(char)
        new_char_index = (char_index + self.offset + self.alphabetLength) % self.alphabetLength
        return self.alphabet[new_char_index]
