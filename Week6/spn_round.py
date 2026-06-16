from sbox_substitution import substitute, inverse_substitute
from permutation_layer import permute, inverse_permute

def spn_round(data, round_key, round_num):
    print(f"\n--- Round {round_num} ---")
    print(f"Input      : {data} (binary: {bin(data)})")
    
    # Step 1: Key Mixing - XOR with round key
    after_key = data ^ round_key
    print(f"After XOR  : {after_key} (binary: {bin(after_key)})")
    
    # Step 2: Substitution - S-Box lookup
    after_sub = substitute(after_key)
    print(f"After S-Box: {after_sub} (binary: {bin(after_sub)})")
    
    # Step 3: Permutation - rearrange bits
    after_perm = permute(after_sub)
    print(f"After Perm : {after_perm} (binary: {bin(after_perm)})")
    
    return after_perm

def inverse_spn_round(data, round_key, round_num):
    # Reverse permutation
    after_perm = inverse_permute(data)
    # Reverse substitution
    after_sub = inverse_substitute(after_perm)
    # Reverse key mixing
    after_key = after_sub ^ round_key
    return after_key

print("=" * 50)
print("   SecureVault - SPN Round Execution")
print("=" * 50)

plaintext = 0b10110010
round_key = 0b01001101

print(f"\nPlaintext  : {plaintext} (binary: {bin(plaintext)})")
print(f"Round Key  : {round_key} (binary: {bin(round_key)})")

# Run one round
encrypted = spn_round(plaintext, round_key, 1)

print(f"\nFinal Output: {encrypted} (binary: {bin(encrypted)})")

# Verify decryption
decrypted = inverse_spn_round(encrypted, round_key, 1)
print(f"Decrypted   : {decrypted} (binary: {bin(decrypted)})")
print(f"Match       : {'SUCCESS' if decrypted == plaintext else 'FAILED'}")
print("\nStatus: Single SPN round operational.")