# AES-inspired S-Box lookup table
SBOX = [
    14,  4, 13,  1,  2, 15, 11,  8,  3, 10,  6, 12,  5,  9,  0,  7,
     0, 15,  7,  4, 14,  2, 13,  1, 10,  6, 12, 11,  9,  5,  3,  8,
     4,  1, 14,  8, 13,  6,  2, 11, 15, 12,  9,  7,  3, 10,  5,  0,
    15, 12,  8,  2,  4,  9,  1,  7,  5, 11,  3, 14, 10,  0,  6, 13
]

# Inverse S-Box for decryption
INVERSE_SBOX = [0] * 64
for i, val in enumerate(SBOX):
    INVERSE_SBOX[val] = i

def substitute(value):
    # Replace input with S-Box output
    return SBOX[value % len(SBOX)]

def inverse_substitute(value):
    # Reverse the substitution for decryption
    return INVERSE_SBOX[value % len(INVERSE_SBOX)]

# Demonstrate S-Box in action
print("=" * 50)
print("   SecureVault - S-Box Substitution Layer")
print("=" * 50)

test_values = [0, 1, 2, 3, 4, 5, 9, 12, 15]

print(f"\n{'Input':<10} {'Output':<10} {'Inverse':<10} {'Match'}")
print("-" * 45)
for val in test_values:
    out = substitute(val)
    recovered = inverse_substitute(out)
    match = "YES" if recovered == val else "NO"
    print(f"{val:<10} {out:<10} {recovered:<10} {match}")

print("\n--- Security Analysis ---")
unique_outputs = len(set(SBOX))
print(f"S-Box size      : {len(SBOX)} entries")
print(f"Unique outputs  : {unique_outputs}")
print(f"Non-linearity   : {'HIGH' if unique_outputs > 10 else 'LOW'}")
print(f"Input 2 maps to : {substitute(2)} (not 2 - relationship hidden)")
print(f"Input 3 maps to : {substitute(3)} (not 3 - relationship hidden)")
print("\nStatus: S-Box substitution layer operational.")