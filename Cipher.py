class Cipher:
    processMethod = None

    def __init__(self, process_method) -> None:
        self.processMethod = process_method

    def encrypt(self, text) -> str:
        encrypted_text = ""

        for char in text:
            try:
                encrypted_text += self.processMethod.process(char)
            except ValueError:
                return "Some characters in text are not included in alphabet"

        return encrypted_text
