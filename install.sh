#!/bin/env bash

set -echo

read -r -p "This script requires root permissions, please acknowledge that it is being run as root. [y|n]: "

if ! [[ $REPLY =~ ^[Yy]$ ]]
then
    echo "Aborting"
    exit 1
fi

echo "Updating script permissions..."
chmod u+x src/template_gen.py

echo "Linking to bin..."
sudo ln src/template_gen.py /usr/local/bin/template_gen

echo "Done, Enjoy :)"