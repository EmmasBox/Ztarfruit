#Zstarfruit for RACF
#Dependencies: Python >=3.12.x and >=ZOAU 1.3.x
#Utility to sort through output from IRRDBU00 and create reports in various formats

from zoautil_py import datasets
from datetime import datetime
import os
import json
import tomllib
import re
import argparse
import sqlite3

parser = argparse.ArgumentParser(
    prog='Ztarfruit for RACF',
    description='Utility to sort through output from IRRDBU100 and create json output',
)

#Flags and arguments to specify in the command line
parser.add_argument('-i', '--input')
parser.add_argument('-r', '--reset')
parser.add_argument('-o', '--obfuscate', action='store_true')

now = datetime.now() # current date and time
date_time = now.strftime("d-%m-%d-%Y-t-%H-%M-%S")
log_name = f"ztarfruit_{date_time}_"

#load settings from razz.toml
with open("zfruit.toml", "rb") as f:
    settings = tomllib.load(f)

database_settings = settings["database"]

#Database name
database_name = database_settings["name"]
con = sqlite3.connect(f"{database_name}.db")

db_cursor = con.cursor()