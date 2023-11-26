from typing import Callable, TypeVar
from functools import wraps
from inspect import get_annotations

RT = TypeVar('RT')

def autotest() -> Callable[[Callable[..., RT]], Callable[..., RT]]:
    def inner(func: Callable[..., RT]) -> Callable[..., RT]:
        
        func.test_from_function = True
        args_template: str = "Argumentos: {} \nTipo de retorno: {}"

        arguments = ""
        return_type = ""

        for k, v in get_annotations(func).items():
            if k != "return":
                arguments += f"\n {k}: {v.__name__}"
                continue
            return_type += f"\n {v.__name__}"
        func.arguments = args_template.format(arguments, return_type)
        
        @wraps(func)
        def wrapper(*args, **kwargs) -> RT:
            return func(*args, **kwargs)
        return wrapper
    return inner