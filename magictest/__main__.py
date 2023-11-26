import os
import click
import inspect
import importlib
from magictest.magictest import MagicTest
from dotenv import load_dotenv

from magictest.types.function_data import FunctionData

load_dotenv()

@click.group()
def cli():
    pass

@cli.command()
@click.option('--inputfile', help='Python file name with directory.')
@click.option('--outputfile', help='Proto buffer file name with directory.')
def generate(inputfile, outputfile):
    path, _ = os.path.splitext(inputfile)
    file_name = path.split('/')[-1]
    module = importlib.import_module(file_name, path)
    functions = inspect.getmembers(module, inspect.isfunction)
    
    magictest = MagicTest(os.getenv("OPENAI_API_KEY"), outputfile)
    tests = ""

    for func in functions:
        if hasattr(func[1], "test_from_function"):
            func_data = FunctionData(name=func[0], doc=func[1].__doc__, args=func[1].arguments)
            tests += magictest.generate_test(func_data)

    ruta_carpeta = os.path.join(os.getcwdb().decode('utf-8'), "tests")
    if not os.path.exists(ruta_carpeta):
        os.makedirs(ruta_carpeta)
    with open(outputfile, "a") as file:
        file.write(tests)


if __name__ == "__main__":
    cli()