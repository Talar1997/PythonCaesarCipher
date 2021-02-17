from Cipher import Cipher
from CaesarCharProc import CaesarCharProc


def is_input_valid(message, offset) -> bool:
    try:
        int(offset)
    except ValueError:
        return False

    return True


def do_encryption(message, offset):
    alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ "
    process_method = CaesarCharProc(alphabet, offset)
    cipher = Cipher(process_method)
    encrypted_message = cipher.encrypt(message)
    print(f'Encrypted: {encrypted_message}')


if __name__ == '__main__':
    message = input("Enter message to encrypt: ")
    offset = input("Enter offset: ")

    if is_input_valid(message, offset):
        do_encryption(message, offset)
    else:
        print("Prompted values are incorrect")
