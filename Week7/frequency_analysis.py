from collections import Counter

def caesar_encrypt(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - base + shift) % 26 + base)
        else:
            result += char
    return result

def frequency_analysis(text):
    letters = [c.upper() for c in text if c.isalpha()]
    total = len(letters)
    counts = Counter(letters)
    return {char: (count/total)*100 
            for char, count in counts.most_common(8)}

def detect_shift(ciphertext):
    # Most frequent letter in English is E
    # Find most frequent in ciphertext and calculate shift
    letters = [c.upper() for c in ciphertext if c.isalpha()]
    counts = Counter(letters)
    most_common = counts.most_common(1)[0][0]
    shift = (ord(most_common) - ord('E')) % 26
    return shift

print("=" * 55)
print("   SecureVault - Frequency Analysis Attack")
print("=" * 55)

plaintext = """Cryptography is the practice of securing 
communications from attackers who want to read 
private messages between two parties"""

shift = 13
ciphertext = caesar_encrypt(plaintext, shift)

print(f"\nOriginal text (first 50 chars): {plaintext[:50]}...")
print(f"Encryption shift used: {shift}")
print(f"Ciphertext (first 50 chars): {ciphertext[:50]}...")

print(f"\n--- Frequency Analysis ---")
freq = frequency_analysis(ciphertext)
print(f"{'Letter':<10} {'Frequency':>12}")
print("-" * 25)
for char, pct in freq.items():
    bar = "█" * int(pct)
    print(f"{char:<10} {pct:>8.1f}%  {bar}")

detected_shift = detect_shift(ciphertext)
cracked = caesar_encrypt(ciphertext, -detected_shift)

print(f"\n--- Attack Result ---")
print(f"Detected shift : {detected_shift}")
print(f"Cracked text   : {cracked[:50]}...")
print(f"Attack success : {'YES' if detected_shift == shift else 'PARTIAL'}")
print("\nConclusion: Caesar cipher broken using letter frequency alone")
print("AES and SPN destroy frequency patterns making this impossible")
print("\nStatus: Frequency analysis attack complete.")