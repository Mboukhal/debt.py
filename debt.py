#!/usr/bin/env python3

import os
import time
import pandas as pd


# cmd = ''
# templete = {
# 	'Name':[],
# 	'Debt':[],
# 	'Date':[]
# 	}


# else:
# 	df = pd.DataFrame(templete, )
# 	df.to_csv('debt.csv')

# def read_csv(file):
# 	df = pd.read_csv(file)
# 	d = df.to_dict("split")
# 	# d = dict(zip(d["index"], d["data"]))
# 	return d
def main():
	cmd = ''
	def add_to_csv():
		# new_row['Name'] = (input('Enter Name:\n\t'))
		# new_row['Debt'] = (input('Enter debt:\n\t') + ' $')
		# date_c = time.strftime("%d-%m-%Y %H:%M")
		# new_row['Date'] = (input(f'Enter date default [{date_c}]:\n\t') or date_c)
		new_row = { 'Name':[], 'Debt':[], 'Date':[] }
		new_row['Name'] = ['kai']
		new_row['Debt'] = ['20$']
		date_c = time.strftime("%d-%m-%Y %H:%M")
		new_row['Date'] = [date_c]
	
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
			# if os.name == 'posix': # if mac os
			os.system("/bin/bash -c 'read -s -n 1 -p \"Press any key to continue...\"'")
			# elif os.name == 'nt': # if windows
				# os.system("pause")
			return
		print ("No file named \{debt.csv\}")
		
	def print_list():
		if os.path.exists('debt.csv'):
			df = pd.read_csv('debt.csv')
			print(df.tail(5))
			print('\n')
			return
		print ("No file named \{debt.csv\}")
		# print(f['columns'])
	
	def delet_from_csv():
		pass
	
	while cmd != 'q':
		os.system('clear')
		print_list()
		# exit(0)
		print("\t1. Add debt.")
		print("\t2. Delet debt.")
		print("\t3. List debt.")
		print("\t4. To quit.")
		print('\n')
		cmd = input('>> ')
		# cmd = '1'
		if cmd == '1':
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