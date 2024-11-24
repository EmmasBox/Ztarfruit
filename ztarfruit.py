#Zstarfruit for RACF
#Dependencies: Python >=3.12.x and >=ZOAU 1.3.x
#Utility to parse output from IRRDBU00 and offer the data through an API

from zoautil_py import datasets
from dataclasses import dataclass
from datetime import datetime
import os
import json
import tomllib
import re
import argparse
import sqlalchemy 
from enum import Enum

parser = argparse.ArgumentParser(
    prog='Ztarfruit for RACF',
    description=
    'Utility to sort through output from IRRDBU100 and serve it through an API'
    ,
)

#Flags and arguments to specify in the command line
parser.add_argument('-i', '--input')
parser.add_argument('-r', '--reset')
parser.add_argument('-o', '--obfuscate', action='store_true')

args = parser.parse_args()

now = datetime.now() # current date and time
date_time = now.strftime("d-%m-%d-%Y-t-%H-%M-%S")
log_name = f"ztarfruit_{date_time}_"

#load settings from zfruit.toml
with open("zfruit.toml", "rb") as f:
    settings = tomllib.load(f)

data_settings = settings["data"]
output_settings = settings["output"]

#Input dataset to parse
input_dataset = args.input or data_settings["input_dataset"]

class Record:
    """Defines a record type that can be parsed, i.e. Group basic data record, 0100"""
    def __init__(self,name: str,identifier: str, fields: list):
        self.name = name
        self.identifier = identifier
        self.fields = fields

class DataType(Enum):
    Char = 1
    Int = 2
    Date = 3
    Time = 4

@dataclass
class Field:
    """The field class is used when defining a record type, it specifies when a field starts and ends"""
    name: str
    data_type: DataType
    start: int
    end: int

    def get_range(self):
        return (self.start, self.end)