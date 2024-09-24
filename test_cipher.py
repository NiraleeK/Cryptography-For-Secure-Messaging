# test_cipher.py

import time
import timeit
import random
import string
from divide_and_conquer_cipher import encrypt_divide_and_conquer, decrypt_divide_and_conquer
from dynamic_search_cipher import encrypt_dynamic_search, decrypt_dynamic_search


def generate_random_message(length):
    return ''.join(random.choices(string.ascii_letters + string.digits + string.punctuation + ' ', k=length))


def measure_time(func, *args):
    setup_code = f"from __main__ import {func.__name__}"
    stmt = f"{func.__name__}(*{args})"
    execution_time = timeit.timeit(stmt, setup=setup_code, number=1)
    result = func(*args)
    return result, execution_time

def test_divide_and_conquer():
    key = 3

    print("\nTesting Divide and Conquer Approach:")

    # Test Case 1: Same Key and Message
    print("Test Case 1: Same Key and Message")
    same_message = "SameMessage123"
    print("Original Message:", same_message)

    # Encryption
    encrypted_message, encryption_time = measure_time(encrypt_divide_and_conquer, same_message, key)
    print("Encrypted Message:", encrypted_message)
    print(f"Encryption Time: {encryption_time:.6f} seconds")

    # Decryption
    decrypted_message, decryption_time = measure_time(decrypt_divide_and_conquer, encrypted_message, key)
    print("Decrypted Message:", decrypted_message)
    print(f"Decryption Time: {decryption_time:.6f} seconds")

    # Test Case 2: Different Key and Message
    print("\nTest Case 2: Different Key and Message")
    different_message = generate_random_message(500)
    different_key = 5
    print("Original Message:", different_message)

    # Encryption
    encrypted_message, encryption_time = measure_time(encrypt_divide_and_conquer, different_message, different_key)
    print("Encrypted Message:", encrypted_message)
    print(f"Encryption Time: {encryption_time:.6f} seconds")

    # Decryption
    decrypted_message, decryption_time = measure_time(decrypt_divide_and_conquer, encrypted_message, different_key)
    print("Decrypted Message:", decrypted_message)
    print(f"Decryption Time: {decryption_time:.6f} seconds")

    # Test Case 3: Repetitive Patterns
    print("\nTest Case 3: Repetitive Patterns")
    repetitive_message = "RepetitivePatterns123ABC" * 10  # Repeat the pattern 10 times
    print("Original Message:", repetitive_message)

    # Encryption
    encrypted_message, encryption_time = measure_time(encrypt_divide_and_conquer, repetitive_message, key)
    print("Encrypted Message:", encrypted_message)
    print(f"Encryption Time: {encryption_time:.6f} seconds")

    # Decryption
    decrypted_message, decryption_time = measure_time(decrypt_divide_and_conquer, encrypted_message, key)
    print("Decrypted Message:", decrypted_message)
    print(f"Decryption Time: {decryption_time:.6f} seconds")

    # Test Case 4: Key Sensitivity
    print("\nTest Case 4: Key Sensitivity")
    key_sensitivity_message = generate_random_message(500)
    print("Original Message:", key_sensitivity_message)

    # Encryption and Decryption with Small Key
    small_key = 1
    print(f"\nUsing Small Key: {small_key}")
    encrypted_message, encryption_time = measure_time(encrypt_divide_and_conquer, key_sensitivity_message, small_key)
    decrypted_message, decryption_time = measure_time(decrypt_divide_and_conquer, encrypted_message, small_key)
    print("Encrypted Message:", encrypted_message)
    print(f"Encryption Time: {encryption_time:.6f} seconds")
    print("Decrypted Message:", decrypted_message)
    print(f"Decryption Time: {decryption_time:.6f} seconds")

    # Encryption and Decryption with Large Key
    large_key = 100
    print(f"\nUsing Large Key: {large_key}")
    encrypted_message, encryption_time = measure_time(encrypt_divide_and_conquer, key_sensitivity_message, large_key)
    decrypted_message, decryption_time = measure_time(decrypt_divide_and_conquer, encrypted_message, large_key)
    print("Encrypted Message:", encrypted_message)
    print(f"Encryption Time: {encryption_time:.6f} seconds")
    print("Decrypted Message:", decrypted_message)
    print(f"Decryption Time: {decryption_time:.6f} seconds")

    # Test Case 5: Performance Evaluation
    print("\nTest Case 5: Performance Evaluation")

    message_lengths = [100, 1000, 10000]
    for length in message_lengths:
        performance_message = generate_random_message(length)
        print(f"\nMessage Length: {length} characters")
        print("Original Message:", performance_message)

        # Encryption
        encrypted_message, encryption_time = measure_time(encrypt_divide_and_conquer, performance_message, key)
        print("Encrypted Message:", encrypted_message)
        print(f"Encryption Time: {encryption_time:.6f} seconds")

        # Decryption
        decrypted_message, decryption_time = measure_time(decrypt_divide_and_conquer, encrypted_message, key)
        print("Decrypted Message:", decrypted_message)
        print(f"Decryption Time: {decryption_time:.6f} seconds")

    # Test Case 6: Known Plaintext Attack Test
    print("\nTest Case 6: Known Plaintext Attack Test")

    known_plaintext_message = "This is a known plaintext message for testing purposes."
    print("Original Message:", known_plaintext_message)

    # Encryption
    encrypted_message, encryption_time = measure_time(encrypt_divide_and_conquer, known_plaintext_message, key)
    print("Encrypted Message:", encrypted_message)
    print(f"Encryption Time: {encryption_time:.6f} seconds")

    # Known Ciphertext (for the known plaintext)
    known_ciphertext = encrypt_divide_and_conquer(known_plaintext_message, key)
    print("Known Ciphertext:", known_ciphertext)

    # Decryption (attempting to deduce the key)
    decrypted_message, decryption_time = measure_time(decrypt_divide_and_conquer, known_ciphertext, key)
    print("Decrypted Message:", decrypted_message)
    print(f"Decryption Time: {decryption_time:.6f} seconds")

    # Test Case 7: Security Evaluation
    print("\nTest Case 7: Security Evaluation")

    # Brute Force Attack
    brute_force_key = 0
    brute_force_message = generate_random_message(500)
    print(f"\nBrute Force Attack with Key: {brute_force_key}")
    print("Original Message:", brute_force_message)
    # Encryption with a different key
    encrypted_message, _ = measure_time(encrypt_divide_and_conquer, brute_force_message, key)

    # Brute force decryption attempt
    decrypted_message, decryption_time = measure_time(decrypt_divide_and_conquer, encrypted_message,
                                                          brute_force_key)
    print("Decrypted Message (Brute Force):", decrypted_message)
    print(f"Decryption Time: {decryption_time:.6f} seconds")

    # Frequency Analysis (assuming the attacker knows the language distribution)
    frequency_analysis_message = generate_random_message(500)
    print("\nFrequency Analysis Attack")
    print("Original Message:", frequency_analysis_message)

    # Encryption
    encrypted_message, _ = measure_time(encrypt_divide_and_conquer, frequency_analysis_message, key)

    # Frequency analysis decryption attempt
    decrypted_message, decryption_time = measure_time(decrypt_divide_and_conquer, encrypted_message, key)
    print("Decrypted Message (Frequency Analysis):", decrypted_message)
    print(f"Decryption Time: {decryption_time:.6f} seconds")

    # Chosen Plaintext Attack (assuming the attacker can choose plaintext and observe ciphertext)
    chosen_plaintext_message = generate_random_message(500)
    print("\nChosen Plaintext Attack")
    print("Original Message:", chosen_plaintext_message)

    # Encryption
    encrypted_message, _ = measure_time(encrypt_divide_and_conquer, chosen_plaintext_message, key)

    # Chosen plaintext decryption attempt
    decrypted_message, decryption_time = measure_time(decrypt_divide_and_conquer, encrypted_message, key)
    print("Decrypted Message (Chosen Plaintext Attack):", decrypted_message)
    print(f"Decryption Time: {decryption_time:.6f} seconds")


def test_dynamic_search():
    key = 3

    print("\nTesting Dynamic Search Algorithm:")

    # Test Case 1: Same Key and Message
    print("Test Case 1: Same Key and Message")
    same_message = "SameMessage123"
    print("Original Message:", same_message)

    # Encryption
    encrypted_message, encryption_time = measure_time(encrypt_dynamic_search, same_message, key)
    print("Encrypted Message:", encrypted_message)
    print(f"Encryption Time: {encryption_time:.6f} seconds")

    # Decryption
    decrypted_message, decryption_time = measure_time(decrypt_dynamic_search, encrypted_message, key)
    print("Decrypted Message:", decrypted_message)
    print(f"Decryption Time: {decryption_time:.6f} seconds")

    # Test Case 2: Different Key and Message
    print("\nTest Case 2: Different Key and Message")
    different_message = generate_random_message(500)
    different_key = 5
    print("Original Message:", different_message)

    # Encryption
    encrypted_message, encryption_time = measure_time(encrypt_dynamic_search, different_message, different_key)
    print("Encrypted Message:", encrypted_message)
    print(f"Encryption Time: {encryption_time:.6f} seconds")

    # Decryption
    decrypted_message, decryption_time = measure_time(decrypt_dynamic_search, encrypted_message, different_key)
    print("Decrypted Message:", decrypted_message)
    print(f"Decryption Time: {decryption_time:.6f} seconds")

    # Test Case 3: Repetitive Patterns
    print("\nTest Case 3: Repetitive Patterns")
    repetitive_message = "RepetitivePatterns123ABC" * 10  # Repeat the pattern 10 times
    print("Original Message:", repetitive_message)

    # Encryption
    encrypted_message, encryption_time = measure_time(encrypt_dynamic_search, repetitive_message, key)
    print("Encrypted Message:", encrypted_message)
    print(f"Encryption Time: {encryption_time:.6f} seconds")

    # Decryption
    decrypted_message, decryption_time = measure_time(decrypt_dynamic_search, encrypted_message, key)
    print("Decrypted Message:", decrypted_message)
    print(f"Decryption Time: {decryption_time:.6f} seconds")

    # Test Case 4: Key Sensitivity
    print("\nTest Case 4: Key Sensitivity")
    key_sensitivity_message = generate_random_message(500)
    print("Original Message:", key_sensitivity_message)

    # Encryption and Decryption with Small Key
    small_key = 1
    print(f"\nUsing Small Key: {small_key}")
    encrypted_message, encryption_time = measure_time(encrypt_dynamic_search, key_sensitivity_message, small_key)
    decrypted_message, decryption_time = measure_time(decrypt_dynamic_search, encrypted_message, small_key)
    print("Encrypted Message:", encrypted_message)
    print(f"Encryption Time: {encryption_time:.6f} seconds")
    print("Decrypted Message:", decrypted_message)
    print(f"Decryption Time: {decryption_time:.6f} seconds")

    # Encryption and Decryption with Large Key
    large_key = 100
    print(f"\nUsing Large Key: {large_key}")
    encrypted_message, encryption_time = measure_time(encrypt_dynamic_search, key_sensitivity_message, large_key)
    decrypted_message, decryption_time = measure_time(decrypt_dynamic_search, encrypted_message, large_key)
    print("Encrypted Message:", encrypted_message)
    print(f"Encryption Time: {encryption_time:.6f} seconds")
    print("Decrypted Message:", decrypted_message)
    print(f"Decryption Time: {decryption_time:.6f} seconds")

    # Test Case 5: Performance Evaluation
    print("\nTest Case 5: Performance Evaluation")

    message_lengths = [100, 1000, 10000]
    for length in message_lengths:
        performance_message = generate_random_message(length)
        print(f"\nMessage Length: {length} characters")
        print("Original Message:", performance_message)

        # Encryption
        encrypted_message, encryption_time = measure_time(encrypt_dynamic_search, performance_message, key)
        print("Encrypted Message:", encrypted_message)
        print(f"Encryption Time: {encryption_time:.6f} seconds")

        # Decryption
        decrypted_message, decryption_time = measure_time(decrypt_dynamic_search, encrypted_message, key)
        print("Decrypted Message:", decrypted_message)
        print(f"Decryption Time: {decryption_time:.6f} seconds")

        # Test Case 6: Known Plaintext Attack Test
    print("\nTest Case 6: Known Plaintext Attack Test")

    known_plaintext_message = "This is a known plaintext message for testing purposes."
    print("Original Message:", known_plaintext_message)

    # Encryption
    encrypted_message, encryption_time = measure_time(encrypt_dynamic_search, known_plaintext_message, key)
    print("Encrypted Message:", encrypted_message)
    print(f"Encryption Time: {encryption_time:.6f} seconds")

    # Known Ciphertext (for the known plaintext)
    known_ciphertext = encrypt_dynamic_search(known_plaintext_message, key)
    print("Known Ciphertext:", known_ciphertext)

    # Decryption (attempting to deduce the key)
    decrypted_message, decryption_time = measure_time(decrypt_dynamic_search, known_ciphertext, key)
    print("Decrypted Message:", decrypted_message)
    print(f"Decryption Time: {decryption_time:.6f} seconds")

    # Test Case 7: Security Evaluation
    print("\nTest Case 7: Security Evaluation")

    # Brute Force Attack
    brute_force_key = 0
    brute_force_message = generate_random_message(500)
    print(f"\nBrute Force Attack with Key: {brute_force_key}")
    print("Original Message:", brute_force_message)

    # Encryption with a different key
    encrypted_message, _ = measure_time(encrypt_dynamic_search, brute_force_message, key)

    # Brute force decryption attempt
    decrypted_message, decryption_time = measure_time(decrypt_dynamic_search, encrypted_message, brute_force_key)
    print("Decrypted Message (Brute Force):", decrypted_message)
    print(f"Decryption Time: {decryption_time:.6f} seconds")

    # Frequency Analysis (assuming the attacker knows the language distribution)
    frequency_analysis_message = generate_random_message(500)
    print("\nFrequency Analysis Attack")
    print("Original Message:", frequency_analysis_message)

    # Encryption
    encrypted_message, _ = measure_time(encrypt_dynamic_search, frequency_analysis_message, key)

    # Frequency analysis decryption attempt
    decrypted_message, decryption_time = measure_time(decrypt_dynamic_search, encrypted_message, key)
    print("Decrypted Message (Frequency Analysis):", decrypted_message)
    print(f"Decryption Time: {decryption_time:.6f} seconds")

    # Chosen Plaintext Attack (assuming the attacker can choose plaintext and observe ciphertext)
    chosen_plaintext_message = generate_random_message(500)
    print("\nChosen Plaintext Attack")
    print("Original Message:", chosen_plaintext_message)

    # Encryption
    encrypted_message, _ = measure_time(encrypt_dynamic_search, chosen_plaintext_message, key)

    # Chosen plaintext decryption attempt
    decrypted_message, decryption_time = measure_time(decrypt_dynamic_search, encrypted_message, key)
    print("Decrypted Message (Chosen Plaintext Attack):", decrypted_message)
    print(f"Decryption Time: {decryption_time:.6f} seconds")

if __name__ == "__main__":
    test_divide_and_conquer()
    test_dynamic_search()
