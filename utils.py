#!/usr/bin/env python3


import os

def clear_console():
	if os.name == 'posix': # if mac os
		os.system('clear')
	elif os.name == 'nt': # if windows
		os.system('cls')

def pause(msg):
	if os.name == 'posix': # if mac os
		os.system(f"/bin/bash -c 'read -s -n 1 -p \"{msg}\"'")
	elif os.name == 'nt': # if windows
		os.system(f"echo \"{msg}\" &pause>nul")