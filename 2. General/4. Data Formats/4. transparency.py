from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization
from cryptography import x509
from cryptography.hazmat.primitives.asymmetric import rsa


""" 
First get the exponent of transparency.pem file

Then get the subdomains of cryptohack.org using openssl s_client -showcerts -connect url:port
example: openssl s_client -showcerts -connect cryptohack.org:443

 """


""" Modulus of Selected File: 234216222856413414056336168901504137710714927916626192370155326892712092546752552141877728
3514380180903995101678237667997337678269553316727281714803494615529102258845811689644913054795785963060141702940653771
36977222164841265084046694925746517387007853236278038029670978141921557139882067656772559964537465702212036054646836981397
59068201745805643226602309648177720842369737425307662674524530757570626970232537549824005998393609021861773134215542450556
839250804799098903483152012713520167414613141526302727512388972623173809195225592109964416682348203058784103484962051844890
398766510080562420295832329553237528041393
Exponent of Selected File: 65537 """


def pemfileread(pemfilename):
    with open(pemfilename, 'rb') as pem_file:
        pem_data = pem_file.read()

    # Load the public key
    public_key = serialization.load_pem_public_key(pem_data, backend=default_backend())

    pem_modulus = public_key.public_numbers().n

    pem_exponent = public_key.public_numbers().e

    return pem_modulus, pem_exponent



def certificateread(certificatefilename):

    # Load the X.509 certificate
    with open(certificatefilename, "rb") as f:
        cert_data = f.read()

    certificate = x509.load_pem_x509_certificate(cert_data, default_backend())

    # Extract the public key
    public_key = certificate.public_key()

    # Extract the public key components (modulus 'n' and public exponent 'e') for RSA
    if isinstance(public_key, rsa.RSAPublicKey):
        cert_modulus = public_key.public_numbers().n
        cert_exponent = public_key.public_numbers().e
        return cert_modulus, cert_exponent
    else:
        print("The public key is not RSA.")
        return 0



def main():
    while True:
        try:
            selection = int(input("Enter your choice: \n1. PEM Public Key File Read\n2. Certificate Read\n"))
        except ValueError:
            print("Invalid input. Please enter a valid integer choice.")
            continue

        if selection == 1:
            pemfilename = input("Enter the filename with extension: ")
            pem_modulus, pem_exponent = pemfileread(pemfilename)
            print(f"Modulus of Selected File: {pem_modulus}")
            print(f"Exponent of Selected File: {pem_exponent}")
            break  # Exit the loop after successful execution
        elif selection == 2:
            certificatefilename = input("Enter the filename with extension: ")
            cert_modulus, cert_exponent = certificateread(certificatefilename)
            print(f"Modulus of Selected File: {cert_modulus}")
            print(f"Exponent of Selected File: {cert_exponent}")
            break  # Exit the loop after successful execution
        else:
            print("Invalid Choice\n")

if __name__ == "__main__":
    main()