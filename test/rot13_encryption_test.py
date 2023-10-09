import string

def rot13enc(message):

    str1 = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
    str2 = 'NOPQRSTUVWXYZABCDEFGHIJKLMnopqrstuvwxyzabcdefghijklm'
    str12 = message.maketrans(str1, str2)

    return message.translate(str12)

def rot13dec(message):

    str1 = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
    str2 = 'NOPQRSTUVWXYZABCDEFGHIJKLMnopqrstuvwxyzabcdefghijklm'
    str12 = message.maketrans(str2, str1)

    return message.translate(str12)


def main():

    print(rot13enc(message))


while True:
    message = rot13enc(input(" --> "))
    print("returning encrypted message")
    print(message)
    rot13dec(message)
    print("returning decrypted message")
    print(rot13dec(message))