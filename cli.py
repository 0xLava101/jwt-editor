from typer import Typer , Option 
from rich.traceback import install


from core.console.rich import ConosoleRich
from core.jwt_manager import JWTManger
from core.algorithms import Algorithm

from typing import Optional

from utils import validate_dict_str_arg

install()

rich        = ConosoleRich()
jwt_manager = JWTManger()


app = Typer(
    invoke_without_command=True,
    epilog=f"[i b]Simple JWT CLI Editor Tool[/]"
)

@app.callback()
def startup(no_banner : bool = Option(False, "--no-banner", help="Disable banner")): 
    """ startup function """
    if not no_banner : 
        rich.banner()

@app.command("decode",help="decode jwt & print it's data")
def decode_token(
    jwt_token : str,
): 

    rich.console.print("[[main]*[/]] [b]Encoded JWT[/] :\n")
    rich.print_jwt(jwt_token)

    token_data = jwt_manager.decode_jwt(jwt_token)

    rich.console.print("[[main]*[/]] [b]Decoded JWT[/] :\n")
    rich.print_decoded_paylaod(token_data)

@app.command("verify",help="verify jwt with algorithm & secret")
def verify_jwt(
    jwt_token : str,
    algorithm : Algorithm = Option(help="JWT Verification Algorithm"),
    secret    : str = Option(help="JWT Secret")
): 
    rich.console.print("[[main]*[/]] [b]Encoded JWT[/] :\n")
    rich.print_jwt(jwt_token)

    token_data = jwt_manager.verify_token(jwt_token, secret, algorithm)
    
    rich.console.print("[[main]*[/]] [b]Decoded JWT[/] :\n")
    rich.print_decoded_paylaod(token_data)

@app.command("modify",help="modify jwt token values with & without secret")
def modify_jwt(
    jwt_token  : str,
    header     : Optional[str] = Option(help="jwt header fields to modify",callback=validate_dict_str_arg,default={}),
    payload    : Optional[str] = Option(help="jwt payload fields to modify",callback=validate_dict_str_arg,default={}),
    secret     : Optional[str] = Option(help="JWT Secret",default="")
): 
    if secret : 
        new_token = jwt_manager.modify_with_secret(jwt_token,header,payload,secret)  
    else : 
        new_token = jwt_manager.modify_without_secret(jwt_token,header,payload) 
    
    rich.console.print("[[main]*[/]] [b]Encoded old JWT[/] :\n")
    rich.print_jwt(jwt_token)

    token_data = jwt_manager.decode_jwt(jwt_token)
        
    rich.console.print("[[main]*[/]] [b]Decoded old JWT[/] :\n")
    rich.print_decoded_paylaod(token_data)

    rich.console.print("[[main]*[/]] [b]Encoded new JWT[/] :\n")
    rich.print_jwt(new_token)

    token_data = jwt_manager.decode_jwt(new_token)

    rich.console.print("[[main]*[/]] [b]Decoded new JWT[/] :\n")
    rich.print_decoded_paylaod(token_data)

if __name__ == '__main__': 
    app()