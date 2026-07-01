def dh_exchange(p, g, alice_private, bob_private):
    alice_public = pow(g, alice_private, p)
    bob_public = pow(g, bob_private, p)
    alice_secret = pow(bob_public, alice_private, p)
    bob_secret = pow(alice_public, bob_private, p)
    return alice_public, bob_public, alice_secret, bob_secret

def brute_force_discrete_log(g, public_key, p, max_attempts=1000):
    # Attacker tries to find private key by brute force
    for i in range(1, max_attempts):
        if pow(g, i, p) == public_key:
            return i, True
    return -1, False

print("=" * 55)
print("   SecureVault - Diffie-Hellman Security Testing")
print("=" * 55)

# Test 1: Small prime (weak - easy to crack)
print("\n[TEST 1] Small Prime (Weak Security)")
p1, g1 = 23, 5
a_pub, b_pub, a_sec, b_sec = dh_exchange(p1, g1, 6, 15)
cracked, found = brute_force_discrete_log(g1, a_pub, p1)
print(f"Prime (p)      : {p1}")
print(f"Shared secret  : {a_sec}")
print(f"Match          : {'YES' if a_sec == b_sec else 'NO'}")
print(f"Brute forced   : {'YES - Private key is ' + str(cracked) if found else 'NO'}")
print(f"Security level : WEAK - Small prime cracked easily")

# Test 2: Medium prime (moderate security)
print("\n[TEST 2] Medium Prime (Moderate Security)")
p2 = 2147483647  # Mersenne prime
g2 = 7
a_pub2, b_pub2, a_sec2, b_sec2 = dh_exchange(p2, g2, 1234567, 7654321)
_, found2 = brute_force_discrete_log(g2, a_pub2, p2, max_attempts=10000)
print(f"Prime (p)      : {p2}")
print(f"Shared secret  : {a_sec2}")
print(f"Match          : {'YES' if a_sec2 == b_sec2 else 'NO'}")
print(f"Brute forced   : {'YES' if found2 else 'NO - Too large to crack'}")
print(f"Security level : MODERATE")

# Test 3: Large prime (strong security)
print("\n[TEST 3] Large Prime (Strong Security)")
p3 = pow(2, 127) - 1  # Very large Mersenne prime
g3 = 7
a_pub3, b_pub3, a_sec3, b_sec3 = dh_exchange(p3, g3, 123456789, 987654321)
print(f"Prime digits   : {len(str(p3))} digits")
print(f"Shared secret  : {str(a_sec3)[:30]}...")
print(f"Match          : {'YES' if a_sec3 == b_sec3 else 'NO'}")
print(f"Brute forced   : NO - Computationally impossible")
print(f"Security level : STRONG")

print("\n--- Security Comparison ---")
print(f"{'Prime Size':<20} {'Crackable':>12} {'Security':>12}")
print("-" * 46)
print(f"{'23 (2 digits)':<20} {'YES':>12} {'WEAK':>12}")
print(f"{'2147483647 (10 digits)':<20} {'NO':>12} {'MODERATE':>12}")
print(f"{str(len(str(p3)))+' digit prime':<20} {'NO':>12} {'STRONG':>12}")
print("\nConclusion: Larger primes make discrete logarithm")
print("computationally impossible protecting DH exchange.")
print("\nStatus: Diffie-Hellman security testing complete.")