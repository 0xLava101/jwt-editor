# core/jwt_manager.py

import json
import jwt 
import warnings

import base64

from core.console.rich import ConosoleRich


warnings.filterwarnings(
    "ignore",
    category=jwt.warnings.InsecureKeyLengthWarning,
)


class JWTManger: 
    def __init__(self): 
        self.console = ConosoleRich()

    def decode_jwt(self, token : str) -> dict | None : 
        try : 
            header = jwt.get_unverified_header(token)
            payload = jwt.decode(
                token,
                options={
                    "verify_signature": False
                }
            )
            return {
                'header'  : header,
                'payload' : payload
            }
        
        except jwt.DecodeError: 
            self.console.error_and_exit("Unvalid JWT Token Faild To Decode It")
    
    def verify_token(self, token: str, secret: str, algorithm: str) -> dict | None:
        try:
            header = jwt.get_unverified_header(token)
            payload = jwt.decode(
                token,
                secret,
                algorithms=[algorithm],
            )

            return {
                'header'  : header,
                'payload' : payload
            }
        
        except jwt.InvalidTokenError as e:
            self.console.error_and_exit(e)

    def decode_segment(self, segment: str) -> dict:
        segment += "=" * (-len(segment) % 4)

        return json.loads(
            base64.urlsafe_b64decode(segment)
        )
    
    def modify_without_secret(self, token : str, new_header : dict, new_payload : dict) -> str: 
        header_b64, payload_b64, signature = token.split(".")
        
        header  = self.decode_segment(header_b64)
        payload = self.decode_segment(payload_b64)

        header.update(new_header)
        payload.update(new_payload)

        new_payload_b64 = base64.urlsafe_b64encode(
            json.dumps(
                    payload,
                    separators=(",", ":")
                ).encode()
        ).decode().rstrip("=")

        new_header_b64 = base64.urlsafe_b64encode(
            json.dumps(
                    header,
                    separators=(",", ":")
                ).encode()
        ).decode().rstrip("=")

        return f"{new_header_b64}.{new_payload_b64}.{signature}"

    def modify_with_secret(self, token : str, new_header : dict, new_payload : dict, secret : str) -> str:
        header_b64, payload_b64, signature = token.split(".")

        header  = self.decode_segment(header_b64)
        payload = self.decode_segment(payload_b64)

        header.update(new_header)
        payload.update(new_payload) 

        algorithm = header.get('alg').lower()

        new_token = jwt.encode(
            payload,
            secret if algorithm != 'none' else None,
            algorithm=algorithm,
            headers=header
        )

        return new_token