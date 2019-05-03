import os
import csv

#1. takes file list of total files (all ctrls)
#2. takes list of partial genes/files (subset of files)
#3. For each gene in subset, finds matching file from total
#4. prints ctrl list


#label_1 = list want
#label_2 = list of total

with open('190503_geneList.csv', mode='rt') as input_file1:	#mode=rt, not rb
	with open('DUB_guides.csv', mode='rt') as input_file2: 
		csv_reader_1 = csv.reader(input_file1, delimiter=',')
		csv_reader_2 = csv.reader(input_file2, delimiter=',')

		total_list2 = []
		for line in csv_reader_2:
			total_list2.append(line)

		print(total_list2) #list of control files (a list of lists)

		final_list = []	

		for row in csv_reader_1:
			row = str(row)

			gene_end = row.find('_')
			gene_symbol = row[2:gene_end] #gets gene symbol

			finalfile = next((s for s in total_list2 if gene_symbol in s), None)
			if finalfile is not None:
				finalfile = [item.strip('\'') for item in finalfile]
				final_list.append(finalfile)
			else:
				print(finalfile)

		with open('output.csv', 'w', newline='') as writeFile:
			writer = csv.writer(writeFile, delimiter=',')

			for item in final_list:
				if item:
					writer.writerow(item)
