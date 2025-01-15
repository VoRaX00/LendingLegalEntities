import datetime

from fastapi import HTTPException
from jose import jwt, JWTError
from rest_framework.request import Request

from service.exceptions.internal_server import InternalServerException
from service.exceptions.unauthorized import UnAuthorized


class TokenManager:
    @staticmethod
    def create_token(data: dict):
        to_encode = data.copy()
        expire = datetime.datetime.now(datetime.timezone.utc) + datetime.timedelta(days=30)
        to_encode.update({"exp": expire})
        auth_data = {
            "secret_key": "oeaibjonbis-ij93rjfpa",
            "algorithm": "HS256",
        }

        encode_jwt = jwt.encode(to_encode, auth_data['secret_key'], algorithm="HS256")
        return encode_jwt

    @staticmethod
    def get_token(request: Request):
        token = request.headers.get("Authorization")
        if not token:
            raise UnAuthorized()
        return token

    @staticmethod
    def decode_token(token: str):
        payload = ''
        try:
            payload = jwt.decode(token, 'oeaibjonbis-ij93rjfpa', algorithms=['HS256'])
        except JWTError:
            raise InternalServerException()
        return payload
