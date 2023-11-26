import os
import re
import openai
from magicaitest.types.function_data import FunctionData


class MagicAITest:

    def __init__(self, openai_api_key: str, outputfile: str) -> None:
        self.openai_api_key = openai_api_key
        self.outputfile = outputfile
        self.max_tests_for_function: int = 3
        self.template = """Genera {} tests en python usando pytest para la funcion: "{}" 
            que tiene la siguiente descripcion: {} y recibe: {}.
            Solo debes mostrar como resultado el codigo que este listo para copiar en un archivo de texto,
            es decir con sintaxis para un archivo .py
            Respuesta (Solo el codigo separado por bloques de texto dependiendo el numero de tests):
            # Function: (function_name) - test1:
            (python code)
            # Function: (function_name) - test2:
            (python code)
            # Function: (function_name) - testn:
            (python code)
            """
        os.environ["OPENAI_API_KEY"] = openai_api_key
        openai.api_key = openai_api_key
    

    def generate_test(self, function_data: FunctionData) -> str:
        response = openai.chat.completions.create(
            model="gpt-3.5-turbo-1106",
            messages=[
                {
                    "role": "user",
                    "content": self.template.format(self.max_tests_for_function, function_data.name, function_data.doc, function_data.args)
                }
            ]
        )
        result: str = response.choices[0].message.content
        cleaned_response = re.sub(r'```python', '', result)
        cleaned_response = re.sub(r'```', '', cleaned_response)
        return cleaned_response

