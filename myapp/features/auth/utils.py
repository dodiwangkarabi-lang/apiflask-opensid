import random
import bcrypt

import hashlib

# =====================================================
# merubah pin sebelum di simpan di database
# =====================================================
def hash_pin(pin):
    pin = str(pin)[::-1]        # reverse string
    pin = int(pin)              # cast int
    pin = pin * 77              # kali 77
    pin = str(pin) + '!#@$#%'   # concat salt
    return hashlib.md5(pin.encode()).hexdigest()

def hash_md5(password: str) -> str:
    return hashlib.md5(password.encode()).hexdigest()

# =====================================================
# merubah input password ke hash sebelum di simpan di db (pengguna / admin)
# =====================================================
def hash_password(password: str) -> str:
    """
    Mengubah password plain text menjadi hash bcrypt
    """
    password_bytes = password.encode('utf-8')
    hashed = bcrypt.hashpw(password_bytes, bcrypt.gensalt())
    return hashed.decode('utf-8')

import bcrypt

# =====================================================
# cek password admin
# =====================================================
def check_password(password: str, hashed: str) -> bool:
    """
    Membandingkan password plain dengan hash (admin)
    """
    return bcrypt.checkpw(
        password.encode('utf-8'),
        hashed.encode('utf-8')
    )
    
    
# def check_password(password: str, hashed: str):
#     return bcrypt.checkpw(
#         password.encode(),
#         hashed.encode()
#     )
    
    
def generate_nik():
    return str(random.randint(1000000000000000, 9999999999999999))  # 16 digit