def caesar_cipher(message, shift, mode='encrypt'):
    result = ""
    
    # Adjust the shift for decryption
    if mode == 'decrypt':
        shift = -shift

    # Traverse the message
    for char in message:
        # Encrypt/Decrypt uppercase characters
        if char.isupper():
            result += chr((ord(char) + shift - 65) % 26 + 65)
        # Encrypt/Decrypt lowercase characters
        elif char.islower():
            result += chr((ord(char) + shift - 97) % 26 + 97)
        else:
            # Keep non-alphabetic characters unchanged
            result += char

    return result

# User input
message = input("Enter your message: ")
shift = int(input("Enter the shift value: "))
mode = input("Type 'encrypt' to encrypt or 'decrypt' to decrypt: ").lower()

# Perform the encryption/decryption
result = caesar_cipher(message, shift, mode)

print(f"Result: {result}")
