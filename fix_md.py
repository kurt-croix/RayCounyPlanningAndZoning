#!/usr/bin/env python3
import re

with open('C:/Users/KurtBognar/Downloads/RayCountyZoning/Article_30_Development_Review_Procedures.md', 'r', encoding='utf-8') as f:
    lines = f.readlines()

cleaned = []
for line in lines:
    s = line.strip()
    
    if re.match(r'^\d+\.\s{2,}[A-Z]', s) and not s.startswith('**'):
        s = re.sub(r'\s{2,}', ' ', s)
        s = f'**{s}**'
        cleaned.append(s + '\n')
    elif re.match(r'^\d+\.\s+\w', s) and not s.startswith('**') and not s.startswith('(') and len(s) < 60:
        s = re.sub(r'\s{2,}', ' ', s)
        s = f'**{s}**'
        cleaned.append(s + '\n')
    elif not s:
        if len(cleaned) >= 2 and cleaned[-1].strip() == '' and cleaned[-2].strip() == '':
            continue
        cleaned.append('\n')
    else:
        cleaned.append(line)

result = ''.join(cleaned)
result = re.sub(r' +\n', '\n', result)
result = re.sub(r'\n{4,}', '\n\n\n', result)

with open('C:/Users/KurtBognar/Downloads/RayCountyZoning/Article_30_Development_Review_Procedures.md', 'w', encoding='utf-8') as f:
    f.write(result)

print("Formatting fixed!")
