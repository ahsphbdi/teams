from datetime import datetime, timedelta
from jose import jwt
from core.config.jwt import JwtConfig


def create_access_token(data: dict, expires_delta: timedelta | None = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(
            minutes=JwtConfig.ACCESS_TOKEN_EXPIRE_MINUTES
        )
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(
        to_encode, JwtConfig.SECRET_KEY, algorithm=JwtConfig.ALGORITHM
    )
    return encoded_jwt
