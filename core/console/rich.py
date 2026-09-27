# core/console/rich.py 


from rich.console import Console 
from rich.text import Text
from rich.theme import Theme

import json

logo = """ 
[purple] ╦╦ ╦╔╦╗  ╔═╗┌┬┐┬┌┬┐┌─┐┬─┐ [/]
[medium_purple1] ║║║║ ║   ║╣  │││ │ │ │├┬┘[/]
[slate_blue1]╚╝╚╩╝ ╩   ╚═╝─┴┘┴ ┴ └─┘┴└─[/]

[b]Codded By[/] : [b red]0xLava101[/]
"""

theme = Theme({
    'main'          : '#875fff',
    'jwt_header'    : 'orange_red1',
    'jwt_payload'   : '#875fff',
    'jwt_signature' : 'chartreuse1',
    'dot_sperator'  : 'dark_slate_gray1'
})


class ConosoleRich: 
    def __init__(self):
        self.console = Console(theme=theme)
    
    def banner(self): 
        self.console.clear()
        self.console.print(logo,justify="center")

    def print_jwt(self, jwt : str): 
        header, payload, signature = jwt.split(".", 2)
        printable_jwt = Text()

        printable_jwt.append(header,style='jwt_header')
        printable_jwt.append('.',style='dot_sperator')
        printable_jwt.append(payload,style='jwt_payload')
        printable_jwt.append('.',style='dot_sperator')
        printable_jwt.append(signature,'jwt_signature')

        self.console.print(printable_jwt,end='\n\n')
    
    def print_decoded_paylaod(self, decoded_jwt : dict): 
        self.console.print_json(json.dumps(decoded_jwt))
        print('\n')

    def print_error(self, error_message : str): 
        self.console.print(f"\n[[red]ERROR[/]] [b]{error_message}[/]\n")

    def error_and_exit(self,error_message): 
        self.print_error(error_message)
        exit(1)