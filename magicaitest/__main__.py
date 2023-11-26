import os
import click
import inspect
import importlib
from magicaitest.magicaitest import MagicAITest
from dotenv import load_dotenv

from magicaitest.types.function_data import FunctionData

load_dotenv()

@click.group()
def cli():
    pass

@cli.command()
@click.option('--inputfile', help='Input file')
@click.option('--outputfile', help='Output file')
@click.option('--openai_model', help='Openai model')
@click.option('--max_test_for_function', help='Maximun number of tests for function')
def generate(inputfile, outputfile, openai_model, max_test_for_function):

    path, _ = os.path.splitext(inputfile)
    module = importlib.import_module(path)
    functions = inspect.getmembers(module, inspect.isfunction)
    
    magicaitest = MagicAITest(os.getenv("OPENAI_API_KEY"), outputfile)
    tests = ""

    for func in functions:
        if hasattr(func[1], "test_from_function"):
            func_data = FunctionData(name=func[0], doc=func[1].__doc__, args=func[1].arguments)
            tests += magicaitest.generate_test(func_data)

    file_name = path.split('.')[-1]
    path_tests_folder = os.path.join(os.getcwdb().decode('utf-8'), "tests")
    path_tests_file = os.path.join(os.getcwdb().decode('utf-8'), "tests", f"test_{file_name}.py")
    
    if not os.path.exists(path_tests_folder):
        os.makedirs(path_tests_folder)
    with open(path_tests_file, "a") as file:
        file.write(tests)


if __name__ == "__main__":
    cli()