def encrypt_caesar(plaintext, key):
    """Encrypts the plaintext using the Caesar cipher."""
    ciphertext = ""
    for char in plaintext:
        if char.isalpha():
            shift = ord(char) + key
            if char.islower():
                if shift > ord('z'):
                    shift -= 26
                ciphertext += chr(shift)
            else:
                if shift > ord('Z'):
                    shift -= 26
                ciphertext += chr(shift)
        else:
            ciphertext += char
    return ciphertext

def decrypt_caesar(ciphertext, key):
    """Decrypts the ciphertext using the Caesar cipher."""
    plaintext = ""
    for char in ciphertext:
        if char.isalpha():
            shift = ord(char) - key
            if char.islower():
                if shift < ord('a'):
                    shift += 26
                plaintext += chr(shift)
            else:
                if shift < ord('A'):
                    shift += 26
                plaintext += chr(shift)
        else:
            plaintext += char
    return plaintext

# Example usage
plaintext = "Hello, world!"
key = 3
ciphertext = encrypt_caesar(plaintext, key)
print(f"Ciphertext: {ciphertext}")
decrypted_plaintext = decrypt_caesar(ciphertext, key)
print(f"Decrypted plaintext: {decrypted_plaintext}")
