import base64

value = "72bca9b68fc16ac7beeb8f849dca1d8a783e8acf9679bf9269f7bf"
print("\n")
print(bytes.fromhex(value))
print("\n")
print(base64.b64encode(bytes.fromhex(value)).decode('utf-8'))
print("\n")


#to encode: print(base64.b64encode(value.encode('utf-8')).decode('utf-8'))