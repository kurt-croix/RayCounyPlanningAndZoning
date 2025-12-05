#!/usr/bin/env python3
"""
Clean up Article 30 markdown formatting issues
"""
import re

# Read the file
with open('C:/Users/KurtBognar/Downloads/RayCountyZoning/Article_30_Development_Review_Procedures.md', 
          'r', encoding='utf-8') as f:
    content = f.read()

# Split into lines for processing
lines = content.split('\n')
cleaned_lines = []

for i, line in enines):
    stripped = line.strip()
    
    # Fix numbered headers that should be bold but aren't
    if re.match(r'^\d+\.\s{2,}[A-Z]', stripped) and not stripped.startswith('**'):
        parts = re.split(r'\s{2,}', stripped, 1)
        if len(parts) == 2:
            cleaned_lines.append(f'**{parts[0]} {parts[1]}**')
        else:
            cleaned_lines.append(f'**{stripped}**')
        continue
    
    # Fix numbered items that look like headers
    if re.match(r'^\d+\.\s+[Atripped) and not stripped.startswith('**') and not stripped.startswith('('):
        if len(stripped) < 50:
            parts = re.split(r'\s{2,}', stripped, 1)
            if len(parts) == 2:
                cleaned_lines.append(f'**{parts[0]} {parts[1]}**')
            else:
                cleaned_lines.append(f'**{stripped}**')
            continue
    
    # Fix short numbered lines that are likely headers
    if re.match(r'^\d+\.\s+[A-Z]', stripped) and not stripped.startswith('**'):
     len(stripped) < 60:
            parts = re.split(r'\s{2,}', stripped, 1)
            if len(parts) == 2:
                cleaned_lines.append(f'**{parts[0]} {parts[1]}**')
            else:
                cleaned_lines.append(f'**{stripped}**')
            continue
    
    # Fix lowercase items - consistent spacing
    if re.match(r'^[a-z]\.\s+', stripped):
        fixed = re.sub(r'^([a-z]\.)\s+', r'\1 ', stripped)
        cleaned_lines.append(fixed)
        continue
    
    # Fix excessive blank lines
   t stripped:
        if len(cleaned_lines) >= 2:
            if cleaned_lines[-1].strip() == '' and cleaned_lines[-2].strip() == '':
                continue
    
    # Keep the line as is
    cleaned_lines.append(line)

# Join back together
result = '\n'.join(cleaned_lines)

# Additional cleanup
result = re.sub(r' +\n', '\n', result)
result = re.sub(r'\n{4,}', '\n\n\n', result)

# Write the cleaned content
with open('C:/Users/KurtBognar/Downloads/RayCountyZoning/Article_30_Developmview_Procedures.md', 
          'w', encoding='utf-8') as f:
    f.write(result)

print("Done! Cleaned up Article 30 markdown formatting")
print(f"Processed {len(lines)} lines")
