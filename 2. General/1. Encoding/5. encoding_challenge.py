from pwn import * # pip install pwntools
import json
import codecs
from Crypto.Util.number import long_to_bytes

r = remote('socket.cryptohack.org', 13377, level = 'debug')

def json_recv():
    line = r.recvline()
    return json.loads(line.decode())

def json_send(hsh):
    request = json.dumps(hsh).encode()
    r.sendline(request)



def decode(encoded_text, encoded_type):
    if encoded_type == "base64":
        return bytes(base64.b64decode(encoded_text)).decode('utf-8')
    
    elif encoded_type == "hex":
        return bytes.fromhex(encoded_text).decode('utf-8')
    
    elif encoded_type == "rot13":
        return codecs.decode(encoded_text, 'rot_13')
    
    elif encoded_type == "bigint":
        return bytes(long_to_bytes(int(encoded_text, 16))).decode('utf-8')

    elif encoded_type == "utf-8":
        return ''.join(chr(i) for i in encoded_text)

for i in range(100):
    received = json_recv()
    encoded_type = received["type"]
    encoded_text = received["encoded"]
    to_send = {
        "decoded": decode(encoded_text, encoded_type)
    }
    json_send(to_send)
print(json_recv())