import re
import sys

filename = sys.argv[1].split()

filename1 = filename[0]
filename2 = filename[1]

file1_contents = {}

with (open(filename1, 'rt') as file1,
      open(filename2, 'rt') as file2,
      open('../diff.txt', 'wt') as diff_file):
    for line in file1:
        code, value = re.split(r'[\t ]+', line.rstrip('\n'))
        file1_contents[value] = code
    
    for line in file2:
        code, value = re.split(r'[\t ]+', line.rstrip('\n'))
        if value not in file1_contents:
            diff_file.write(line)
