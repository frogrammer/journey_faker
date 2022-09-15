# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring
# pylint: disable=line-too-long
import json
from typing import Union

def read_json(file: str):
    f = []
    with open(file, 'r', encoding='UTF-8') as fh:
        f = json.loads(fh.read())
    return f

def write_json(file: str, dict: Union[dict, list]):
    with open(file, 'w', encoding='UTF-8') as fh:
        fh.write(json.dumps(dict))