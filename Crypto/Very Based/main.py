from base64 import b64decode, b32decode

def decode_base64():
    string = 'SU5FVkk2WlhHSlJXT1MyTUdORFZFSkJFTEJSRzRLVDU='
    decoded_string = b64decode(string).decode('utf-8')
    return decoded_string

def decode_base32():
    string2 = 'INEVI6ZXGJRWOS2MGNDVEJBELBRG4KT5'
    decoded_string2 = b32decode(string2).decode('utf-8')
    return decoded_string2


def main():
    print(decode_base64())
    print(decode_base32())


if __name__ == "__main__":
    main()
