import requests
import base64
import os
import re


def main():
    os.chdir(os.path.dirname(__file__))
    GFWLIST_URL = 'https://raw.githubusercontent.com/gfwlist/gfwlist/master/gfwlist.txt'
    contents = requests.get(GFWLIST_URL).text
    contents = base64.b64decode(contents)
    lines = contents.split(b'\n')
    with open('myrules.txt', 'rb') as f:
        myrule = f.read()
    with open('gfwlist.my.txt', 'wb') as f:
        write = f.write
        write(lines[0])
        write(b'\n\n')
        write(myrule)
        write(b'\n\n')

        for i in range(1, len(lines)):
            l = lines[i]
            if l.startswith(b'!'):
                continue
            write(l)
            write(b'\n')


if __name__ == '__main__':
    main()
