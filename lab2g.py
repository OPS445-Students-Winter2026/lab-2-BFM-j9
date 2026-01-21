#!/usr/bin/env python3
#Author: Jude O
#Author ID: 103399176
#Date: 2026/01/20

import sys

if len(sys.argv) < 2:
	timer = 3
else:
     timer = int(sys.argv[1])

while timer > 0:
	print(timer)
	timer = timer - 1

print('blast off!')
