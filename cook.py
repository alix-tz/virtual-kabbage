# encoding: utf-8

import json
import os
import numpy as np

import argparse


# get arguments from command line
parser = argparse.ArgumentParser()
parser.add_argument("-i", required=True, help="input file (must be a csv)")
parser.add_argument("-auth", help="addition author information (formart: Firstname Lastname <email>)")
parser.add_argument("-k", help="keyboard name")
args = parser.parse_args()

# welcome message
from art import tprint
from termcolor import cprint
print("\nWelcome to\n")
tprint("Virtual Kabbage", font="smshadow")
cprint("A virtual-keyboard generator for eScriptorium\n", "green")

proceed = True
# check if input ends with .csv
if not args.i.endswith(".csv"):
    cprint("Input file must be a csv", "red")
    proceed = False  

# check if input file exists
if not os.path.exists(args.i):
    cprint("File not found", "red")
    proceed = False

if proceed:
    # get file basename and output path
    path = args.i
    basename = os.path.basename(path).split(".")[0]
    output_path = path.replace(".csv", ".json")
    
    # read keyboard layout from csv
    kbd_layout = np.genfromtxt(path, delimiter=',', dtype=None, encoding="utf8")
    print("Keyboard layout successfully loaded")
    print("Keyboard dimension will be", kbd_layout.shape[0], "x", kbd_layout.shape[1])

    # add author information to json file
    if args.auth:
        author = f"Virtual Kabbage & {args.auth}"
    else:
        author = "Virtual Kabbage"

    # add keyboard name to json file
    if args.k:
        keyboard_name = args.k
    else:
        keyboard_name = basename

    # create base for json file
    kbd = {"version": "0.1",
            "name": keyboard_name,
            "author": author,
            "characters": []}

    # add characters to json file
    for row in range(kbd_layout.shape[0]):
        for column in range(kbd_layout.shape[1]):
            if kbd_layout[row, column]:
                character = {"row": row,
                            "column": column,
                            "character": kbd_layout[row, column],
                            "keyboard_code": None}
                kbd["characters"].append(character)
    
    # write json file
    with open(output_path, "w", encoding="utf8") as f:
        json.dump(kbd, f, ensure_ascii=False, indent=4)
        print("Keyboard layout successfully written to", output_path)
     

