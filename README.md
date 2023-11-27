# AITestGen
Python Library to generate unit tests using OpenAI API

## Installation
### Create a virtual enviroment (Optional)
```bash
python -m venv venv
source venv/bin/activate # venv/Scripts/activate on Windows
```
### Install package (require python ^3.11 version)
```bash
pip install aitestgen
```

### Add OpenAI API Key (Required)
```bash
export OPENAI_API_KEY=<my_api_key>  # or add variable in your .env file
```

## Example
Create a python file and add the following code:
```python
from aitestgen.autotest import autotest

@autotest()
def sum(num1: float, num2: float) -> float:
    """This function is responsible for calculating the sum of two numbers"""
    return num1 + num2

@autotest()
def mul(num1: float, num2: float) -> float:
    """This function is responsible for calculating the multiplication of two numbers"""
    return num1 * num2
```

### Important:
To improve results, add type annotations and documentation to the function.

## Generate tests:

Run the following command (change the filename)
```bash
aitestgen generate --inputfile src/operations.py
```

And then you will get the following result in a .py file created in a tests folder:

## Result
```python

# Function: mul - test1:
def test_mul_positive_numbers():
    assert mul(5.5, 2) == 11.0

# Function: mul - test2:
def test_mul_negative_numbers():
    assert mul(-3, 4) == -12.0

# Function: mul - test3:
def test_mul_zero():
    assert mul(0, 10) == 0.0

# Function: sum - test1:
def test_sum_positive_numbers():
    assert sum(3.5, 2.5) == 6.0

# Function: sum - test2:
def test_sum_negative_numbers():
    assert sum(-3.5, -2.5) == -6.0

# Function: sum - test3:
def test_sum_mixed_numbers():
    assert sum(3.5, -2.5) == 1.0

```
