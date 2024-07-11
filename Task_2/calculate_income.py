from typing import Callable
import re

def generator_numbers(text: str):
    for match in re.finditer(r'\b\d+\.\d+\b', text):
        yield float(match.group())

def sum_profit(text: str, func: Callable):
    return sum(func(text))

