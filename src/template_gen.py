# Copyright (c) Brandon Pacewic
# SPDX-License-Identifier: MIT

import os

ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def get_templates():
    while True:
        if os.path.exists('templates'):
            templates = [os.path.join('templates', f) for f in os.listdir('templates')]
            break

        os.chdir('../')

    return templates


def user_select_template(templates):
    for i, template in enumerate(templates):
        print(f'{i + 1}: {template.split(os.sep)[-1]}')

    return templates[int(input('Enter the number of the template you want to use: ')) - 1]


def main():
    start_directory = os.getcwd() + os.sep
    templates = get_templates()
    template = user_select_template(templates)
    generation_option = input('Count or Name [c/n]: ').lower()

    if generation_option == 'c':
        count = int(input('How many files do you want to generate: '))
        for i in range(count):
            os.system(f'copy {template} {start_directory}{ALPHABET[i]}.{template.split(".")[-1]}')
    else:
        name = input('What do you want to name the file: ')
        os.system(f'copy {template} {start_directory}{name}.{template.split(".")[-1]}')


if __name__ == '__main__':
    main()
