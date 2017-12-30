#!/usr/bin/env python3
import requests
import base64
import os
import re


def main():
    os.chdir(os.path.dirname(os.path.realpath(__file__)))
    GFWLIST_URL = 'https://raw.githubusercontent.com/gfwlist/gfwlist/master/gfwlist.txt'
    contents = requests.get(GFWLIST_URL).content
    contents = base64.b64decode(contents)
    lines = contents.split(b'\n')
    with open('myrules.txt', 'rb') as f:
        myrules = f.readlines()

    lines = [l + b'\n' for l in lines if not l.startswith(b'!') and not l.startswith(b'@@')]
    lines[1:1] = myrules
    unique_lines = set(lines)

    with open('gfwlist.my.txt', 'wb') as f:
        write = f.write
        for l in lines:
            if l in unique_lines:
                write(l)
                unique_lines.discard(l)


if __name__ == '__main__':
    main()
