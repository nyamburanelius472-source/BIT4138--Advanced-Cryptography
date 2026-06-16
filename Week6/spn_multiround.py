from spn_round import spn_round, inverse_spn_round

def generate_round_keys(master_key, num_rounds):
    # Generate different key for each round
    round_keys = []
    key = master_key
    for i in range(num_rounds):
        key = (key * 31 + 17) % 256
        round_keys.append(key)
    return round_keys

def multi_round_encrypt(plaintext, master_key, num_rounds=4):
    round_keys = generate_round_keys(master_key, num_rounds)
    data = plaintext
    for i in range(num_rounds):
        data = spn_round(data, round_keys[i], i + 1)
    return data, round_keys

def multi_round_decrypt(ciphertext, round_keys):
    data = ciphertext
    for i in reversed(range(len(round_keys))):
        data = inverse_spn_round(data, round_keys[i], i + 1)
    return data

print("=" * 50)
print("   SecureVault - Multi-Round SPN Encryption")
print("=" * 50)

plaintext = 0b10110010
master_key = 0b11001010
num_rounds = 4

print(f"\nPlaintext  : {plaintext} ({bin(plaintext)})")
print(f"Master Key : {master_key} ({bin(master_key)})")
print(f"Rounds     : {num_rounds}")

encrypted, round_keys = multi_round_encrypt(plaintext, master_key, num_rounds)
decrypted = multi_round_decrypt(encrypted, round_keys)

print(f"\n{'='*50}")
print(f"Original  : {plaintext} ({bin(plaintext)})")
print(f"Encrypted : {encrypted} ({bin(encrypted)})")
print(f"Decrypted : {decrypted} ({bin(decrypted)})")
print(f"Match     : {'SUCCESS' if decrypted == plaintext else 'FAILED'}")
print(f"\nRound keys used: {round_keys}")
print("\nStatus: Multi-round SPN encryption operational.")