from pwdlib import PasswordHash
# uv add pwdlib
pwd_context = PasswordHash.recommended()

def crear_hash_password(password:str):
    return pwd_context.hash(password)

def verificar_password(password, hashed_password):
    return pwd_context.verify(password, hashed_password)
