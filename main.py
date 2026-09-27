from core.console.rich import ConosoleRich

import jwt

cn = ConosoleRich()
jwt_token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiYWRtaW4iOnRydWUsImlhdCI6MTUxNjIzOTAyMn0.KMUFsIDTnFmyG3nMiGM6H9FNFUROf3wh7SmqJp-QV30"

cn.banner()

cn.print_jwt(jwt_token)

data = jwt.decode(jwt_token,options={"verify_signature": False})

cn.print_decoded_paylaod(data)