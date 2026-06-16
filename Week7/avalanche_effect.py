import hashlib

def count_different_bits(hash1, hash2):
    diff = 0
    for b1, b2 in zip(hash1, hash2):
        xor = b1 ^ b2
        diff += bin(xor).count('1')
    return diff

def avalanche_test(text1, text2):
    h1 = hashlib.sha256(text1.encode()).digest()
    h2 = hashlib.sha256(text2.encode()).digest()
    diff_bits = count_different_bits(h1, h2)
    total_bits = len(h1) * 8
    percentage = (diff_bits / total_bits) * 100
    return h1.hex(), h2.hex(), diff_bits, total_bits, percentage

print("=" * 55)
print("   SecureVault - Avalanche Effect Demonstration")
print("=" * 55)

test_pairs = [
    ("HELLO", "HELLo"),
    ("SecureVault", "SecureVauld"),
    ("BIT4138", "BIT4139"),
    ("Nairobi", "nairobi"),
]

print(f"\n{'Text 1':<15} {'Text 2':<15} {'Bits Changed':>14} {'Percentage':>12}")
print("-" * 60)

for t1, t2 in test_pairs:
    h1, h2, diff, total, pct = avalanche_test(t1, t2)
    strong = "STRONG" if pct >= 45 else "WEAK"
    print(f"{t1:<15} {t2:<15} {diff:>10} bits {pct:>8.1f}% {strong}")

print("\n--- Detailed Example ---")
t1, t2 = "HELLO", "HELLo"
h1, h2, diff, total, pct = avalanche_test(t1, t2)
print(f"Input 1 : {t1}")
print(f"Input 2 : {t2}")
print(f"Hash 1  : {h1[:32]}...")
print(f"Hash 2  : {h2[:32]}...")
print(f"Changed : {diff} out of {total} bits ({pct:.1f}%)")
print("\nConclusion: One character change scrambles over 50% of output")
print("This makes pattern-based attacks practically impossible")
print("\nStatus: Avalanche effect demonstration complete.")