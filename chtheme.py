#!/usr/bin/python

import os
import sys

# fs options
output_file = "./config.h"
input_template = "./config.def.h"
themes_dir = "./themes/"

# tag options
open_tag = "// THEME_START"
close_tag = "// THEME_END"

themes = []

config_start = []
config_theme = []
config_end = []

def usage():
    msg = """chtheme.py - Change st themes with a simple tool.
Works by adding the text from .theme files located in the theme directory.

example:
    python chtheme.py THEME_NAME > ./config.h

    where THEME_NAME is a file in the themes directory.
    """
    print(msg)

def exit():
    usage()
    sys.exit(2)

def parse_def_config():
    with open(input_template) as f:
        for line in f:
            config_start.append(line)
            if open_tag in line:
                for line in f:
                    # throw away these lines between tags
                    if close_tag in line:
                        config_end.append(line)
                        for line in f:
                            config_end.append(line)

def output_config_file():
    with open(output_file, 'w+') as f:
        f.writelines(config_start)
        f.writelines(config_theme)
        f.writelines(config_end)

def output_config_stdout():
    for line in config_start:
        print(line.replace("\n", ""))
    for line in config_theme:
        print(line.replace("\n", ""))
    for line in config_end:
        print(line.replace("\n", ""))

def get_themes():
    for f in os.listdir(themes_dir):
        themes.append(f.split(".")[0])

def get_theme():
    if len(sys.argv) > 1:
        if not sys.argv[1] in themes:
            print("Error! unknown theme!\n")
            exit()
        else:    
            with open("./themes/" + sys.argv[1] + ".theme") as f:
                for line in f:
                    config_theme.append(line)
    else:
        exit()


if __name__ == "__main__":
    get_themes()
    get_theme()
    parse_def_config()
    output_config_stdout()

