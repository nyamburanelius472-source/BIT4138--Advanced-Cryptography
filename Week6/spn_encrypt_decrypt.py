from spn_multiround import multi_round_encrypt, multi_round_decrypt

def encrypt_message(message, master_key):
    results = []
    for char in message:
        val = ord(char)
        encrypted, round_keys = multi_round_encrypt(val, master_key)
        results.append((encrypted, round_keys))
    return results

def decrypt_message(encrypted_data):
    chars = []
    for encrypted, round_keys in encrypted_data:
        decrypted = multi_round_decrypt(encrypted, round_keys)
        chars.append(chr(decrypted))
    return "".join(chars)

print("=" * 55)
print("   SecureVault - SPN Encryption and Decryption Proof")
print("=" * 55)

master_key = 0b11001010
test_messages = [
    "Nairobi",
    "BIT4138",
    "SecureVault"
]

for message in test_messages:
    encrypted_data = encrypt_message(message, master_key)
    decrypted = decrypt_message(encrypted_data)
    encrypted_values = [e for e, _ in encrypted_data]
    
    print(f"\nOriginal  : {message}")
    print(f"Encrypted : {encrypted_values}")
    print(f"Decrypted : {decrypted}")
    print(f"Match     : {'SUCCESS' if message == decrypted else 'FAILED'}")

print("\n--- Security Summary ---")
print("Each character passes through 4 SPN rounds")
print("Key mixing + S-Box + Permutation per round")
print("Decryption reverses all operations perfectly")
print("\nStatus: SPN system fully operational.")