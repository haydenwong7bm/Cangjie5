import re
import sys

filename = sys.argv[1].split()

with (open(filename[0], 'rt', encoding='utf-8') as file,
      open(filename[1], 'wt', encoding='utf-8') as output_q):
    
    code_list = set()
    for line in file:
        code, value = re.split(r'[\t ]+', line.rstrip('\n'))
        
        if code.startswith('zx'):
            code_quick = f'z{code[-1]}'
        elif code[0] == 'z':
            if len(code) >= 5:
                code_quick = f'z{code[1:3]}{code[-1]}'
            else:
                code_quick = code
        elif len(code) > 2:
            code_quick = f'{code[0]}{code[-1]}'
        else:
            code_quick = code
        
        if (code_quick, value) not in code_list:
            output_q.write(f'{code_quick}  {value}\n')
            code_list.add((code_quick, value))
