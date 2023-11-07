#! /usr/bin/python3

# Copyright (c) Brandon Pacewic
# SPDX-License-Identifier: MIT

import os
import sys

ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def main():
    start_directory = os.getcwd() + os.sep
    copy_command = 'copy' if sys.platform == 'win32' else 'cp'

    while True:
        if os.path.exists('templates'):
            templates = [os.path.join('templates', f) for f in os.listdir('templates')]
            break

        os.chdir('../')

    for i, template in enumerate(templates):
        print(f'{i + 1}: {template.split(os.sep)[-1]}')

    template = templates[int(input('Enter the number of the template you want to use: ')) - 1]
    generation_option = input('Count or Name [c/n]: ').lower()

    if generation_option == 'c':
        count = int(input('How many files do you want to generate: '))
        for i in range(count):
            os.system(f'{copy_command} {template} {start_directory}{ALPHABET[i]}.{template.split(".")[-1]}')
    else:
        name = input('What do you want to name the file: ')
        os.system(f'{copy_command} {template} {start_directory}{name}.{template.split(".")[-1]}')


if __name__ == '__main__':
    main()
