import pandas as pd
import numpy as np
import os

def main():

	

	path = input('Enter file path to workbook name and extension, e.g. example.xlsx: ')

	row_count = int ( input ('Enter the row number you want to split the excel sheet at: ') )


	destination = input('Enter folder path to where you want the split files stored. Press Enter to save in current location: ')




	i = 0
	row_count = row_count - 5
	df = pd.read_excel(path) # change this to read_csv if the files is a csv file
	for chunk in np.array_split(df, len(df) // row_count):
		chunk.to_csv(destination + 'file_{:02d}.csv'.format(i), index=False, header=False)
		i += 1

		

	
	

if __name__ == '__main__':
	main()
