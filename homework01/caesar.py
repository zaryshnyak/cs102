"""
    Шифрует открытый текст с помощью шифра Цезаря.
    >>> encrypt_caesar("PYTHON")
    'SBWKRQ'
    >>> encrypt_caesar("python")
    'sbwkrq'
    >>> encrypt_caesar("Python3.6")
    'Sbwkrq3.6'
    >>> encrypt_caesar("")

"""
def encrypt_caesar(plaintext):    
    ciphertext = ''
    for ch in plaintext:
        if 'a' <= ch <= 'z' or 'A' <= ch <= 'Z':
            code = ord(ch) + 3
            if code > ord('Z') and code < ord('a') or code > ord('z'):
                code -= 26
            ciphertext += chr(code)
        else:
            ciphertext += ch
    print (ciphertext)
    return ciphertext
encrypt_caesar("Python3.6")


"""
    Расшифровывает зашифрованный текст, используя шифр Цезаря.
    >>> decrypt_caesar("SBWKRQ")
    'PYTHON'
    >>> decrypt_caesar("sbwkrq")
    'python'
    >>> decrypt_caesar("Sbwkrq3.6")
    'Python3.6'
    >>> decrypt_caesar("")

"""
def decrypt_caesar(ciphertext):
    plaintext = ''
    for ch in ciphertext:
        if 'a' <= ch <= 'z' or 'A' <= ch <= 'Z':
            code = ord(ch) - 3
            if code < ord('a') and code > ord('Z') or code < ord('A'):
                code += 26
            plaintext += chr(code)
        else:
            plaintext += ch
    print (plaintext)
    return plaintext
decrypt_caesar("Sbwkrq3.6")
