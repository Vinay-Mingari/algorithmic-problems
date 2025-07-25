
def encode(message: str, shift: int) -> str:
    """Encodes a string by shifting each letter forward."""
    result = ""
    for char in message:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            shifted = (ord(char) - base + shift) % 26
            result += chr(base + shifted)
        else:
            result += char  # Non-letter characters stay the same
    return result

def decode(message: str, shift: int) -> str:
    """Decodes a string by reversing the Caesar Cipher shift."""
    return encode(message, -shift)

# 🧪 Simple testing
if __name__ == "__main__":
    original = "Hello, Vinay!"
    encoded = encode(original, 3)
    decoded = decode(encoded, 3)

    print("Original:", original)
    print("Encoded :", encoded)
    print("Decoded :", decoded)
