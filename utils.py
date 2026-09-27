# utils.py 

import json 
import typer 

def validate_dict_str_arg(
        ctx: typer.Context,
        param: typer.CallbackParam,
        value : str
) -> dict : 
    try : 
        parameter = json.loads(value)
    except json.JSONDecodeError:
        raise typer.BadParameter(f"{param.name} must be valid JSON")

    if not isinstance(parameter, dict):
        raise typer.BadParameter(
            f"{param.name} must be a JSON object"
        )

    return parameter
