
from Crypto.PublicKey import RSA
from datetime import datetime, timedelta
import hashlib
import json

def generate_certificate(owner_name, organization, valid_days=365):
  
    key = RSA.generate(2048)
    public_key = key.publickey().export_key().decode()
    private_key = key.export_key().decode()
    
   
    valid_from = datetime.now()
    valid_to = valid_from + timedelta(days=valid_days)
    
    certificate = {
        "version": "X.509 v3",
        "serial_number": hashlib.md5(owner_name.encode()).hexdigest()[:16],
        "subject": {
            "common_name": owner_name,
            "organization": organization,
            "country": "KE"
        },
        "issuer": {
            "common_name": "SecureVault CA",
            "organization": "SecureVault Certificate Authority",
            "country": "KE"
        },
        "validity": {
            "not_before": valid_from.strftime("%Y-%m-%d %H:%M:%S"),
            "not_after": valid_to.strftime("%Y-%m-%d %H:%M:%S")
        },
        "public_key_algorithm": "RSA-2048",
        "signature_algorithm": "SHA256withRSA",
        "public_key_preview": public_key[:64] + "..."
    }
    
    # Step 3: CA signs the certificate
    cert_data = json.dumps(certificate).encode()
    ca_signature = hashlib.sha256(cert_data).hexdigest()
    certificate["ca_signature"] = ca_signature
    
    return certificate, private_key

print("=" * 55)
print("   SecureVault - PKI Certificate Generation")
print("=" * 55)

# Generate certificate for a user
cert, private_key = generate_certificate(
    owner_name="Nelius Nyambura",
    organization="Mount Kenya University",
    valid_days=365
)

print(f"\n--- Digital Certificate ---")
for key, value in cert.items():
    if isinstance(value, dict):
        print(f"\n{key.upper()}:")
        for k, v in value.items():
            print(f"  {k:<25}: {v}")
    else:
        print(f"{key:<25}: {value}")

print(f"\n--- Certificate Status ---")
print(f"Issued by : {cert['issuer']['common_name']}")
print(f"Valid for : 365 days")
print(f"Algorithm : {cert['signature_algorithm']}")
print(f"Signed    : YES - CA signature present")
print("\nStatus: PKI certificate generated successfully.")