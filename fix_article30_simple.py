#!/usr/bin/env python3
import re

# Read raw content
with open('C:/Users/KurtBognar/Downloads/RayCountyZoning/article30_extracted_raw.txt', 'r', encoding='utf-8') as f:
    raw = f.read()

# Read existing markdown
with open('C:/Users/KurtBognar/Downloads/RayCountyZoning/Article_30_Development_Review_Procedures.md', 'r', encoding='utf-8') as f:
    existing = f.read()

# Simple conversion - just append the raw with basic formatting
output = [existing.rstrip(), '\n\n']

lines = raw.split('\n')
for i, line in enumerate(lines):
    s = line.strip()
    
    # Main sections
    if re.match(r'^30\.\d+\s+', s):
        output.append(f'\n## {s}\n\n')
    # Uppercase subsections
    elif re.match(r'^[A-Z]\.\s+\w', s):
        output.append(f'\n### {s}\n\n')
    # Numbered items that look like headers
    elif re.match(r'^\d+\.\s+[A-Z]', s) and len(s) > 20:
        output.append(f'\n**{s}**\n\n')
    # Lowercase items
    elif re.match(r'^[a-z]\.\s+', s):
        output.append(f'{s}\n\n')
    # Parenthetirs
    elif re.match(r'^\(\d+\)', s):
        output.append(f'   {s}\n\n')
    # Figure headers
    elif s.startswith('Figure '):
        output.append(f'\n**{s}**\n\n')
    # Regular lines
    elif s:
        output.append(f'{s}\n\n')
    else:
        output.append('\n')

result = ''.join(output)

# Write
with open('C:/Users/KurtBognar/Downloads/RayCountyZoning/Article_30_Development_Review_Procedures.md', 'w', encoding='utf-8') as f:
    f.write(result)

print('DONE! Article 30 is now ')
print(f'Original: {len(existing)} chars')
print(f'Added: {len(result) - len(existing)} chars')
print(f'Final: {len(result)} chars')
