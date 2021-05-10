# caesar cipher
def caesar_encrypt(text_to_encrypt, shift):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    res = []
    len_alphabet = len(alphabet)
    for i in text_to_encrypt:
        res.append(alphabet[(alphabet.find(i) + shift) % len_alphabet])
    return ''.join(res)


def caesar_decrypt(text_to_decrypt, shift):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    res = []
    len_alphabet = len(alphabet)
    for i in text_to_decrypt:
        res.append(alphabet[(alphabet.find(i) - shift) % len_alphabet])
    return ''.join(res)


def atbash_encrypt(text_to_encrypt):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    return text_to_encrypt.translate(str.maketrans(
        alphabet + alphabet.upper(), alphabet[::-1] + alphabet.upper()[::-1]))


def atbash_decrypt(text_to_decrypt):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    return text_to_decrypt.translate(str.maketrans(
        alphabet + alphabet.lower(), alphabet[::-1] + alphabet.lower()[::-1]))
