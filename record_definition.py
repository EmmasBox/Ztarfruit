#This module contains the classes used to define the data structure of the IRRBU00 records

from dataclasses import dataclass
from enum import Enum

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