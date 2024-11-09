import re
import sys

file1_contents = {}

with (open(sys.argv[1], 'rt') as file1,
      open(sys.argv[2], 'rt') as file2,
      open('../diff.txt', 'wt') as diff_file):
    for line in file1:
        code, value = re.split(r'[\t ]+', line.rstrip('\n'))
        file1_contents[value] = code
    
    for line in file2:
        code, value = re.split(r'[\t ]+', line.rstrip('\n'))
        if value not in file1_contents:
            diff_file.write(line)
