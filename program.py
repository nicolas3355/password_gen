import hashlib
import base64

def get_password(key, domain):
    passwd = key.encode('ascii') + domain.encode('ascii')
    for _ in range(0, 1000000):
        passwd = hashlib.sha3_256(passwd).digest()
    return base64.b85encode(passwd)[-16:]
