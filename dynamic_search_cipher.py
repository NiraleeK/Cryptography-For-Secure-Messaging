def encrypt_dynamic_search(message, key):
    encrypted_message = ""

    for char in message:
        encrypted_char = dynamic_search_encrypt(char, key)
        encrypted_message += encrypted_char

    return encrypted_message

def decrypt_dynamic_search(encrypted_message, key):
    decrypted_message = ""

    for encrypted_char in encrypted_message:
        decrypted_char = dynamic_search_decrypt(encrypted_char, key)
        decrypted_message += decrypted_char

    return decrypted_message

def dynamic_search_encrypt(char, key):
    # Implementation of dynamic search algorithm for encryption
    # (Replace this with your actual implementation)
    return chr((ord(char) + key) % 128)

def dynamic_search_decrypt(char, key):
    # Implementation of dynamic search algorithm for decryption
    # (Replace this with your actual implementation)
    return chr((ord(char) - key) % 128)
