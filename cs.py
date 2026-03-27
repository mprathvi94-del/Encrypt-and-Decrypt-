# Caesar Cipher Encryption
def encrypt(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            shift_base = 65 if char.isupper() else 97
            result += chr((ord(char) - shift_base + shift) % 26 + shift_base)
        else:
            result += char
    return result

# Caesar Cipher Decryption
def decrypt(text, shift):
    return encrypt(text, -shift)

# Example
text = input("Enter text: ")
shift = 3

encrypted = encrypt(text, shift)
print("Encrypted:", encrypted)

decrypted = decrypt(encrypted, shift)
print("Decrypted:", decrypted)