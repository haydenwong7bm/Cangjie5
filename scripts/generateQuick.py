import re
import sys

with (open(sys.argv[1], 'rt', encoding='utf-8') as file,
      open(sys.argv[2], 'wt', encoding='utf-8') as output_q):
    
    for _ in range(11):
        output_q.write(file.readline())
    
    code_list = set()
    for line in file:
        value, code = re.split(r'[\t ]+', line.rstrip('\n'))[:2]
        
        if code.startswith('x'): # quick input no code starts with x
            continue
        
        code_quick = f'{code[0]}{code[-1]}'
        
        if (code_quick, value) not in code_list:
            output_q.write(f'{code_quick}\t{value}\n')
            code_list.add((code_quick, value))
