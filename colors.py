#!/usr/bin/python3
import sys

import os

os.system('color')

import colorama

from colorama import init, AnsiToWin32, Fore, Back, Style

colorama.init(wrap=False)

print(Fore.RED, Back.GREEN + 'Dragon Ball is Mid\n')

print(Fore.BLACK, Back.YELLOW + 'MHA is Mid.\n')

print(Fore.WHITE, Style.BRIGHT, Back.BLUE + 'Fairy Tail is Mid\n')

print(Style.RESET_ALL)
