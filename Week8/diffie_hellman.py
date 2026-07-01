
def generate_public_key(g, private_key, p):
    # Formula: public_key = g^private_key mod p
    return pow(g, private_key, p)

def compute_shared_secret(other_public, private_key, p):
    # Formula: secret = other_public^private_key mod p
    return pow(other_public, private_key, p)

print("=" * 55)
print("   SecureVault - Diffie-Hellman Key Exchange")
print("=" * 55)

# Step 1: Public parameters agreed by both parties
p = 23    # Prime number (public)
g = 5     # Generator (public)

print(f"\n[STEP 1] Public Parameters")
print(f"Prime number (p) : {p}")
print(f"Generator (g)    : {g}")
print(f"Both values are known to everyone including attackers")

# Step 2: Private keys chosen secretly
alice_private = 6
bob_private = 15

print(f"\n[STEP 2] Private Keys (Secret)")
print(f"Alice private key: {alice_private} (only Alice knows)")
print(f"Bob private key  : {bob_private} (only Bob knows)")

# Step 3: Generate public keys
alice_public = generate_public_key(g, alice_private, p)
bob_public = generate_public_key(g, bob_private, p)

print(f"\n[STEP 3] Public Keys Generated")
print(f"Alice public key : {alice_public} (sent to Bob)")
print(f"Bob public key   : {bob_public} (sent to Alice)")
print(f"Formula: public = g^private mod p")
print(f"Alice: {g}^{alice_private} mod {p} = {alice_public}")
print(f"Bob  : {g}^{bob_private} mod {p} = {bob_public}")

# Step 4: Compute shared secret
alice_secret = compute_shared_secret(bob_public, alice_private, p)
bob_secret = compute_shared_secret(alice_public, bob_private, p)

print(f"\n[STEP 4] Shared Secret Computed")
print(f"Alice computes: {bob_public}^{alice_private} mod {p} = {alice_secret}")
print(f"Bob computes  : {alice_public}^{bob_private} mod {p} = {bob_secret}")

print(f"\n{'='*55}")
print(f"Alice secret : {alice_secret}")
print(f"Bob secret   : {bob_secret}")
print(f"Match        : {'SUCCESS - Same secret reached independently' if alice_secret == bob_secret else 'FAILED'}")
print(f"\nAttacker sees only: p={p}, g={g}, A={alice_public}, B={bob_public}")
print(f"Cannot determine private keys without solving discrete logarithm")
print("\nStatus: Diffie-Hellman key exchange complete.")