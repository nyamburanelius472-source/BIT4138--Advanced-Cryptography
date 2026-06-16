def simple_cipher(plaintext, key):
    # Weak cipher for demonstration
    result = []
    for char in plaintext:
        val = (ord(char) + key) % 256
        val = val ^ (key << 1) % 256
        result.append(val)
    return result

def compute_difference(cipher1, cipher2):
    return [a ^ b for a, b in zip(cipher1, cipher2)]

def count_bit_differences(val1, val2):
    xor = val1 ^ val2
    return bin(xor).count('1')

print("=" * 55)
print("   SecureVault - Differential Cryptanalysis")
print("=" * 55)

key = 57
message1 = "HELLO"
message2 = "HELLo"  # Only last character changed

print(f"\nMessage 1 : {message1}")
print(f"Message 2 : {message2}")
print(f"Difference: Only last character changed (L→l)")

cipher1 = simple_cipher(message1, key)
cipher2 = simple_cipher(message2, key)
differences = compute_difference(cipher1, cipher2)

print(f"\n{'Char':<8} {'C1':>8} {'C2':>8} {'Diff':>8} {'Bits Changed':>14}")
print("-" * 50)
for i, (c1, c2, d) in enumerate(zip(cipher1, cipher2, differences)):
    bits = count_bit_differences(c1, c2)
    changed = "← changed" if message1[i] != message2[i] else ""
    print(f"{message1[i]:<8} {c1:>8} {c2:>8} {d:>8} {bits:>8} bits {changed}")

total_bits = sum(count_bit_differences(c1, c2) 
                for c1, c2 in zip(cipher1, cipher2))
print(f"\nOne character change caused {total_bits} total bit differences")
print(f"Attacker uses these patterns to deduce key information")
print("\nStatus: Differential cryptanalysis simulation complete.")