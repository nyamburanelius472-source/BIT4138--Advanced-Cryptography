def xor_encrypt(plaintext, key):
    return [ord(c) ^ key for c in plaintext]

def recover_key(plaintext, ciphertext):
    # Attacker knows one plaintext-ciphertext pair
    # and can recover the key mathematically
    recovered = ciphertext[0] ^ ord(plaintext[0])
    return recovered

def verify_key(ciphertext, key):
    return "".join(chr(c ^ key) for c in ciphertext)

print("=" * 55)
print("   SecureVault - Algebraic Attack Simulation")
print("=" * 55)

# Victim encrypts using simple XOR
plaintext = "SecureVault"
key = 42
ciphertext = xor_encrypt(plaintext, key)

print(f"\n[VICTIM SIDE]")
print(f"Plaintext : {plaintext}")
print(f"Secret Key: {key}")
print(f"Ciphertext: {ciphertext}")

print(f"\n[ATTACKER SIDE]")
print(f"Attacker intercepts ciphertext: {ciphertext}")
print(f"Attacker knows one word - guesses first char is 'S'")

recovered_key = recover_key(plaintext[0], ciphertext)
print(f"Recovered Key : {recovered_key}")
print(f"Key Match     : {'YES' if recovered_key == key else 'NO'}")

decrypted = verify_key(ciphertext, recovered_key)
print(f"Decrypted     : {decrypted}")

print("\n--- Why This Attack Works ---")
print("XOR has a mathematical weakness: C = P XOR K")
print("Therefore                      : K = P XOR C")
print("Knowing ANY plaintext-ciphertext pair reveals the key")
print("AES and SPN avoid this using non-linear S-Boxes")
print("\nStatus: Algebraic attack simulation complete.")