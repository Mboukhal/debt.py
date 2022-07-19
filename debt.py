#!/usr/bin/env python3

import os
import time
import pandas as pd

def pause(msg):
	if os.name == 'posix': # if mac os
		os.system(f"/bin/bash -c 'read -s -n 1 -p \"{msg}\"'")
	elif os.name == 'nt': # if windows
		os.system("pause")


def print_list():
	if os.path.exists('debt.csv'):
		df = pd.read_csv('debt.csv')
		print(df.tail(5))
		print('\n')
		return
	print ("No file named \{debt.csv\}")
	
def add_to_csv():
	print_list()
	new_row = { 'Name':[], 'Debt':[], 'Date':[] }
	new_row['Name'] = [(input('Enter Name:\n\t>> '))]
	new_row['Debt'] = [(input('Enter debt:\n\t>> ') + '$')]
	date_c = time.strftime("%d-%m-%Y %H:%M")
	new_row['Date'] = [(input(f'Enter date default [{date_c}]:\n\t>> ') or date_c)]
	new_df = pd.DataFrame(new_row)
	print (new_row)
	if os.path.exists('debt.csv'):
		df = pd.read_csv('debt.csv')
		df = df.append(new_df, ignore_index=True)
		df.to_csv('debt.csv', index=False)
		return
	new_df.to_csv('debt.csv', index=False)
	
def print_list_all():
	if os.path.exists('debt.csv'):
		df = pd.read_csv('debt.csv')
		print(df)
		print('\n')
		pause('Press any key to continue...\n')
		return
	print ("No file named \{debt.csv\}")
	

def delet_from_csv():
	if os.path.exists('debt.csv'):
		df = pd.read_csv('debt.csv')
		print(df)
		print('\n')
		choise = [int(input('Enter id to remove:\n\t>> '))]
		s = df.loc[choise[0]]
		try:
			df.drop(index=choise, axis=0, inplace=True)
		except Exception:
			os.system('clear')
			print(f"Error {choise} not in list!")
			pause()
			return
		print(s)
		pause('\ndeleted.')
		df.to_csv('debt.csv', index=False)
		return
	print ("No file named \{debt.csv\}")

def main():
	cmd = ''
	while cmd != 'q':
		os.system('clear')
		print_list()
		print("\t1. Add debt.")
		print("\t2. Delet debt.")
		print("\t3. List debt.")
		print("\t4. To quit.")
		print()
		cmd = input('>> ')
		if cmd == '1':
			os.system('clear')
			add_to_csv()
		if cmd == '2':
			os.system('clear')
			delet_from_csv()
		if cmd == '3':
			os.system('clear')
			print_list_all()
		if cmd == '4':
			exit(0)
			
if __name__ == '__main__':
	main()