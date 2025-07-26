
def caesar_cipher(text, shift, decode=False):
    result = []
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            offset = -shift if decode else shift
            shifted = (ord(char) - base + offset + 26) % 26 + base
            result.append(chr(shifted))
        else:
            result.append(char)
    return ''.join(result)


print(caesar_cipher("Hello, World!", 3,decode = "True"))

