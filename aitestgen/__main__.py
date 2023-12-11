import os
import click
import inspect
import importlib
from aitestgen.aitestgen import AITestGen
from dotenv import load_dotenv

from aitestgen.types.function_data import FunctionData

load_dotenv()

@click.group()
def cli():
    pass

@cli.command()
@click.option('--inputfile', help='Input file')
def generate(inputfile):

    path, _ = os.path.splitext(inputfile)
    file_name = path.split('/')[-1]

    module_location = os.path.join(os.getcwd(), inputfile)
    spec = importlib.util.spec_from_file_location(file_name, module_location)

    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    functions = inspect.getmembers(module, inspect.isfunction)
    
    aitestgen = AITestGen(os.getenv("OPENAI_API_KEY"))
    tests = ""

    for func in functions:
        if hasattr(func[1], "test_from_function"):
            func_data = FunctionData(name=func[0], doc=func[1].__doc__, args=func[1].arguments)
            tests += aitestgen.generate_test(func_data)

    path_tests_folder = os.path.join(os.getcwd(), "tests")
    if not os.path.exists(path_tests_folder):
        os.makedirs(path_tests_folder)
    with open(path_tests_folder + f"/test_{file_name}.py", "w+") as file:
        file.write(tests)

    print(f"Generated test_{file_name}.py file in tests folder")


if __name__ == "__main__":
    cli()