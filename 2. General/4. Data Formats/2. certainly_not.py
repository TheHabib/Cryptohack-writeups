#This code decodes DER-encoded x509 RSA certificate

from cryptography import x509

with open("certainly_not.der", "rb") as f:
    cert = x509.load_der_x509_certificate(f.read())

modulus = cert.public_key().public_numbers().n
public_exponent = cert.public_key().public_numbers().e

print(f"Modulus is: {modulus}")
print(f"Public Exponent is: {public_exponent}")