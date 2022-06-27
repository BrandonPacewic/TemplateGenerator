#! /usr/bin/python3

import sys
import os

ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
TEMPLATES = '~/Templates/'
CODE_FORCES = 'codeForces.cpp'
GOOGLE_CODE_JAM = 'googleCodeJam.cpp'

class Colors:
    GREEN = '\033[92m'
    RED = '\033[91m'


def make_alphabet(template: str, times: int) -> None:
    for i in range(times):
        os.system(f"cp {TEMPLATES}{template} {ALPHABET[i]}.cpp")


def get_template(template: str) -> str:
    if template == "forces":
        return CODE_FORCES
    elif template == "google":
        return GOOGLE_CODE_JAM
    else:
        return None


def main():
    template = get_template(sys.argv[1])
    try:
        option = int(sys.argv[2])
        make_alphabet(template, option)
    except ValueError:
        os.system(f"cp {TEMPLATES}{template} {sys.argv[2]}")

    print(f"{Colors.GREEN}[FINISHED]")


if __name__ == '__main__':
    main()