"""
    Шифрует открытый текст с помощью шифра Vigenere.
    >>> encrypt_vigenere("PYTHON", "A")
    'PYTHON'
    >>> encrypt_vigenere("python", "a")
    'python'
    >>> encrypt_vigenere("ATTACKATDAWN", "LEMON")
    'LXFOPVEFRNHR'
"""


def encrypt_vigenere(plaintext, keyword):
    ciphertext = ''
    print("Вводим:", plaintext)
    for index, ch in enumerate(plaintext):
        if 'a' <= ch <= 'z' or 'A' <= ch <= 'Z':
            shift = ord(keyword[index % len(keyword)])  # сдвиг,кл.слово,индекс
            shift -= ord('a') if 'a' <= ch <= 'z' else ord('A')
            code = ord(ch) + shift  # код, сдвиг
            if 'a' <= ch <= 'z' and code > ord('z'):
                code -= 26
            elif 'A' <= ch <= 'Z' and code > ord('Z'):
                code -= 26
            ciphertext += chr(code)
        else:  # остальное
            ciphertext += ch
    print("Получаем:", ciphertext)
    return ciphertext  # возврат  зашифрованного текста
encrypt_vigenere("ATTACKATDAWN", "LEMON")

"""
Расшифровывает зашифрованный текст с помощью шифра Видженера.
>>> decrypt_vigenere("PYTHON", "A")
'PYTHON'
>>> decrypt_vigenere("python", "a")
'python'
>>> decrypt_vigenere("LXFOPVEFRNHR", "LEMON")
'ATTACKATDAWN'
"""


def decrypt_vigenere(ciphertext, keyword):
    plaintext = ''
    for index, ch in enumerate(ciphertext):
        if 'a' <= ch <= 'z' or 'A' <= ch <= 'Z':
            shift = ord(keyword[index % len(keyword)])
            shift -= ord('a') if 'a' <= ch <= 'z' else ord('A')
            code = ord(ch) - shift
            if 'a' <= ch <= 'z' and code < ord('a'):
                code += 26
            elif 'A' <= ch <= 'Z' and code < ord('A'):
                code += 26
            plaintext += chr(code)
        else:
            plaintext += ch
    print("Расшифровка", plaintext)
    return plaintext
decrypt_vigenere("LXFOPVEFRNHR", "LEMON")
