from datetime import datetime, timedelta, timezone
from conf import settings
import jwt
from pwdlib import PasswordHash
# uv add pwdlib
pwd_context = PasswordHash.recommended()

def crear_hash_password(password:str):
    return pwd_context.hash(password)

def verificar_password(password, hashed_password):
    return pwd_context.verify(password, hashed_password)

def crear_access_token(data, expires_delta: timedelta | None = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.now(timezone.utc) + expires_delta
    else:
        expire =  datetime.now(timezone.utc) + timedelta(minutes=30)
    
    to_encode.update({"exp":expire})
    #{"sub": "admin",}
    print(settings.SECRET_KEY)
    token = jwt.encode(to_encode, settings.SECRET_KEY,settings.ALGORITHM)
    return token

def verificar_token(token):
    try:
        payload = jwt.decode(token,settings.SECRET_KEY, algorithms=[settings.ALGORITHM] )
        return payload
    except jwt.InvalidTokenError:
        return None
    