data = open("24.txt").read()

import re

my_re = re.compile(r'[A-Z^C^D](?:C|D)')