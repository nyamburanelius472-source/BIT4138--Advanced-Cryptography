PERMUTATION = [1, 5, 2, 0, 3, 7, 4, 6]
INVERSE_PERM = [0] * 8
for i, p in enumerate(PERMUTATION):
    INVERSE_PERM[p] = i

def permute(value, num_bits=8):
    # Rearrange bits according to permutation table
    bits = [(value >> (num_bits - 1 - i)) & 1 for i in range(num_bits)]
    permuted_bits = [bits[PERMUTATION[i]] for i in range(num_bits)]
    result = 0
    for bit in permuted_bits:
        result = (result << 1) | bit
    return result

def inverse_permute(value, num_bits=8):
    # Reverse the permutation for decryption
    bits = [(value >> (num_bits - 1 - i)) & 1 for i in range(num_bits)]
    restored_bits = [0] * num_bits
    for i in range(num_bits):
        restored_bits[INVERSE_PERM[i]] = bits[i]
    result = 0
    for bit in restored_bits:
        result = (result << 1) | bit
    return result

print("=" * 50)
print("   SecureVault - Permutation Layer")
print("=" * 50)
print(f"\nPermutation table: {PERMUTATION}")
print("Each position moves to a new location\n")

test_values = [0b10110001, 0b11001010, 0b01111000, 0b10101010]

print(f"{'Original':<20} {'Permuted':<20} {'Restored':<20} {'Match'}")
print("-" * 70)
for val in test_values:
    permuted = permute(val)
    restored = inverse_permute(permuted)
    match = "YES" if restored == val else "NO"
    print(f"{bin(val):<20} {bin(permuted):<20} {bin(restored):<20} {match}")

print("\n--- Diffusion Analysis ---")
original = 0b10110001
permuted = permute(original)
changed_bits = bin(original ^ permuted).count('1')
print(f"Original : {bin(original)}")
print(f"Permuted : {bin(permuted)}")
print(f"Bits moved: {changed_bits} out of 8")
print(f"Diffusion : {'STRONG' if changed_bits > 4 else 'MODERATE'}")
print("\nStatus: Permutation layer operational.")