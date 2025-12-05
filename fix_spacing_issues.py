import re

# Read the file
with open('Article_30_Development_Review_Procedures.md', 'r', encoding='utf-8') as f:
    content = f.read()

lines = content.split('\n')
output_lines = []

for i, line in enumerate(lines):
    # Remove excessive trailing spaces from headings
    if line.startswith('#'):
        # Remove multiple spaces between # and text, keep only one
        line = re.sub(r'^(#+)\s+', r'\1 ', line)
        # Remove trailing spaces
        line = line.rstrip()
    
    # Fix mixed list formatting - if we see "1." followed by plain text after a #### heading
    # Check context: if previous non-empty line is #### and this line starts with number,
    # it might need to be ##### 
    if re.match(r'^[a-z]\)\s+', line):
        # Letter with parenthesis like "a)" should be plain text, not heading
        output_lines.append(line)
        continue
        
    # Fix cases where there's inconsistent indentation in lists under headings
    if i > 0:
        prev_line = lines[i-1] if i > 0 else ""
        # If previous line was #### and current is "1. " without heading marker
        if re.match(r'^#### ', prev_line) and re.match(r'^1\.\s+', line):
            # This should stay as plain numbered text
            pass
        # If we have "##### b." we should check if there's a "1." before it that's not a heading
        elif re.match(r'^##### [a-z]\.', line):
            # Check backwards for item "1." that should be at same level
            for j in range(i-1, max(0, i-10), -1):
                if re.match(r'^1\.\s+the ', lines[j]):
                    # Found a plain "1." - this "##### b." is at wrong level
                    # It should match the "1." format
                    line = re.sub(r'^##### ([a-z]\.\s+)', r'\1', line)
                    break
    
    output_lines.append(line)

# Write the output
with open('Article_30_Development_Review_Procedures.md', 'w', encoding='utf-8') as f:
    f.write('\n'.join(output_lines))

print("Fixed spacing and formatting issues")
