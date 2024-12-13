#Ztarfruit for RACF
#Dependencies: Python >=3.12.x and >=ZOAU 1.3.x
#Utility to parse output from IRRDBU00 and offer the data through an API

from zoautil_py import datasets
from datetime import datetime
import os
import json
import tomllib
import re
import argparse
import sqlalchemy
from records import database_records

parser = argparse.ArgumentParser(
    prog='Ztarfruit for RACF',
    description=
    'Utility to sort through output from IRRDBU100 and serve it through an API'
    ,
)

#Flags and arguments to specify in the command line
parser.add_argument('-i', '--input')
parser.add_argument('-r', '--reset', action='store_true')
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
    
#This function loads in the IRRDBU00 output, internal function please ignore
def load_input():
    if datasets.exists(input_dataset):
        print("Target dataset exists")
        output = datasets.read(input_dataset)
        return output
    else:
        return ""
        
if input_dataset != "":
    dataset_contents = load_input()
    input_path = "./temp.txt"

    #remove input data in case the utility has been ran before
    if os.path.exists(input_path):
        os.remove(input_path)

    rInput = open(input_path, "a")
    rInput.write(dataset_contents)
    rInput.close()
    print(f"Temp file size: {os.path.getsize(input_path)} bytes")
    