import csv
import os

## parse csv file and retrieve columns data
def get_bug_details(input_path):
	bug_list = []
	line_numbers = []
	suspiciousness_list = []

	with open(input_path, 'r') as file:
		csvreader = csv.reader(file)
		for row in csvreader:
			if ('$' in row[0]):
				bug_list.append(row[0].split('$',1)[0])
			else:
				bug_list.append(row[0])
			line_numbers.append(row[1])
			suspiciousness_list.append(float(row[2]))

	## find rank and duplicate count
	rank_list = []
	duplicate_counts = []
	for i in range(len(bug_list)):
		suspiciousness = suspiciousness_list[i]
		rank = suspiciousness_list.index(suspiciousness) + 1

		count = 0
		for j in range(rank - 1, len(bug_list), 1):
			if suspiciousness_list[j] == suspiciousness:
				count += 1
			else:
				break
		rank_list.append(rank)
		duplicate_counts.append(count)

	return bug_list, line_numbers, suspiciousness_list, rank_list, duplicate_counts


def write_new_csv(bug_list, line_numbers, suspiciousness_list, rank_list, duplicate_counts, output_path):
	f_csv1 = open(output_path, "w", encoding='UTF8', newline='')
	csv_writer1 = csv.writer(f_csv1)
	feature_names = ["file_name", "line_numbers", "suspiciousness", "rank", "duplicate_count"]
	csv_writer1.writerow(feature_names)

	for i in range(len(line_numbers)):
		feature_row = [bug_list[i], line_numbers[i], suspiciousness_list[i], rank_list[i], duplicate_counts[i]]
		csv_writer1.writerow(feature_row)
	f_csv1.close()


## get total number of lines for each suspected buggy file
def get_line_totals(file_path):
	file_serials = []
	line_counts = []

	with open(file_path, 'r') as file:
		csvreader = csv.reader(file)
		flag = False
		for row in csvreader:
			if flag == False:
				flag = True
				continue
			file_serials.append(int(row[0]))
			line_counts.append(int(row[1]))
	return file_serials, line_counts


def get_real_buggy_lines_type1(file_path, arr):
	file = open(file_path, 'r')
	lines = file.readlines()
	for line in lines:
		if "#" in line:
			arr.append(line.split("#")[0].replace(".java", "").replace("/", ".") + "#" + line.split("#")[1])
	return arr


def get_real_buggy_lines_type2(file_path, arr):

	file = open(file_path, 'r')
	content = file.read()
	lines = content.strip().split("\n")
	for line in lines:
		if "," in line:
			parts = line.split(",")
			for part in parts:
				if "#" in part:
					line_str_num = part.split("#")[0].replace(".java", "").replace("/", ".") + "#" + part.split("#")[1]
					if line_str_num not in arr:
						arr.append(line_str_num)
	return arr


def get_top_k(buggy_lines, suspicious_lines, k):
	if len(suspicious_lines) > k:
		k_lines = suspicious_lines[:k]
	else:
		k_lines = suspicious_lines

	count = 0
	for line in buggy_lines:
		if line in k_lines:
			count += 1
	return count*100/len(buggy_lines)


def get_position_k(buggy_lines, suspicious_lines, k):
	i = 0
	for line in suspicious_lines:
		if line in buggy_lines:
			i += 1
			if i == k:
				return line


def get_last_position(buggy_lines, suspicious_lines):
	for i in range(len(suspicious_lines) - 1, -1, -1):
		if suspicious_lines[i] in buggy_lines:
			return suspicious_lines[i]



if __name__ == '__main__':
	f_csv = open("outputs/output_summary.csv", "w", encoding='UTF8', newline='')
	csv_writer = csv.writer(f_csv)
	feature_names = ["suspected_buggy_file", "real_buggy_lines", "top@5", "top@10", "top@20", "top@50", "top@100", "best_case", "avg_case", "worst_case","best_rank"]
	csv_writer.writerow(feature_names)

	## get total number of lines for each suspected buggy file
	file_serials, line_counts = get_line_totals("lines_count.csv")

	dir_suspected = "suspected_buggy_lines"
	dir_real = "real_buggy_lines"

	suspected_buggy_files = os.listdir(dir_suspected)

	for file in suspected_buggy_files:
		file_path = dir_suspected + "/" + file
		if file_path.endswith("slicing.csv"):
			output_path = "outputs/rank_duplicates/" + file
			bug_list, line_numbers, suspiciousness_list, rank_list, duplicate_counts = get_bug_details(file_path)
			prefix = file.split("_")[0].capitalize()
			serial = int(file.split("_")[1])

			combines = []
			for i in range(len(bug_list)):
				combines.append(bug_list[i] + "#" + line_numbers[i])

			total_line_index = file_serials.index(serial)
			total_line = line_counts[total_line_index]

			buggy_lines = []
			file_path1 = dir_real + "/" + prefix + "-" + str(serial) + ".buggy.lines"
			if os.path.exists(file_path1):
				buggy_lines = get_real_buggy_lines_type1(file_path1, buggy_lines)
			file_path2 = dir_real + "/" + prefix + "-" + str(serial) + ".candidates"
			if os.path.exists(file_path2):
				buggy_lines = get_real_buggy_lines_type2(file_path2, buggy_lines)

			if len(buggy_lines) < 1:
				continue
			
			lines_not_found = []
			for line in buggy_lines:
				if line not in combines:
					lines_not_found.append(line)

			rank_unknown = len(rank_list) + 1
			for line in lines_not_found:
				bug_list.append(line.split("#")[0])
				line_numbers.append(line.split("#")[1])
				suspiciousness_list.append(0)
				rank_list.append(rank_unknown)
				duplicate_counts.append(len(lines_not_found))
				combines.append(line)

			write_new_csv(bug_list, line_numbers, suspiciousness_list, rank_list, duplicate_counts, output_path)

			## calculate top@k
			top_5 = get_top_k(buggy_lines, combines, 5)
			top_10 = get_top_k(buggy_lines, combines, 10)
			top_20 = get_top_k(buggy_lines, combines, 20)
			top_50 = get_top_k(buggy_lines, combines, 50)
			top_100 = get_top_k(buggy_lines, combines, 100)

			best_line = get_position_k(buggy_lines, combines, 1)
			best_index = combines.index(best_line)
			best_rank = rank_list[best_index]
			if duplicate_counts[best_index] > 1:
				best_case = (duplicate_counts[best_index]/2 + rank_list[best_index] - 1)/total_line
			else:
				best_case = rank_list[best_index]/total_line
			best_case = round(best_case, 6)

			average_count = len(buggy_lines)//2
			if average_count < 1:
				average_count = 1
			avg_line = get_position_k(buggy_lines, combines, average_count)
			avg_index = combines.index(avg_line)
			if duplicate_counts[avg_index] > 1:
				avg_case = (duplicate_counts[avg_index]/2 + rank_list[avg_index] - 1)/total_line
			else:
				avg_case = rank_list[avg_index]/total_line
			avg_case = round(avg_case, 6)

			last_line = get_last_position(buggy_lines, combines)
			last_index = combines.index(last_line)
      
			if(suspiciousness_list[last_index]!=0):
				worst_case = (total_line-(len(rank_list)+1))/total_line
			else:
				worst_case = (total_line - (rank_list[last_index] + duplicate_counts[last_index]))/total_line
			print(duplicate_counts[last_index])
			print(rank_list[last_index])
			worst_case = round(worst_case, 6)

			feature_row = [prefix + "_" + str(serial), len(buggy_lines), top_5, top_10, top_20, top_50, top_100, best_case, avg_case, worst_case, best_rank]
			csv_writer.writerow(feature_row)
	f_csv.close()


	


	


