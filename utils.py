#!/usr/bin/env python3


from os import name, system

def clear_console():
	if name == 'posix': # if mac os
		system('clear')
	elif name == 'nt': # if windows
		system('cls')

def pause(msg):
	if name == 'posix': # if mac os
		system(f"/bin/bash -c 'read -s -n 1 -p \"{msg}\"'")
	elif name == 'nt': # if windows
		system(f"echo {msg} &pause>nul")

def open_src(path):
	if name == 'posix': # if mac os
		system(f"open {path}")
	elif name == 'nt': # if windows
		system(f"explorer {path}")