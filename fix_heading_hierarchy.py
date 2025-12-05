import re

# Read the file
with open('Article_30_Development_Review_Procedures.md', 'r', encoding='utf-8') as f:
    content = f.read()

lines = content.split('\n')
output_lines = []
i = 0

while i < len(lines):
    line = lines[i]
    
    # Check if this is a ### heading (level 3, like "### C. Fees")
    if re.match(r'^### [A-Z]\. ', line):
        output_lines.append(line)
        i += 1
        
        # Look ahead for numbered items that should be ####
        while i < len(lines):
            next_line = lines[i]
            
            # Bold numbered items like **1. Application Filing Fees** should become ####
            if re.match(r'^\*\*[0-9]+\.\s+', next_line):
                # Extract the text without the bold markers
                text = re.sub(r'^\*\*([0-9]+\.\s+.+?)\*\*$', r'#### \1', next_line)
                output_lines.append(text)
                i += 1
                
                # Look for lettered sub-items (a., b., c.) that should be #####
                while i < len(lines):
                    sub_line = lines[i]
                    
                    # Plain lettered items like "a. Generally" should become #####
                    if re.match(r'^[a-z]\.\s+', sub_line):
                        text = re.sub(r'^([a-z]\.\s+.+)$', r'##### \1', sub_line)
                        output_lines.append(text)
                        i += 1
                    elif re.match(r'^### |^## |^\*\*[0-9]+\. ', sub_line):
                        # Hit another major section, break out
                        break
                    else:
                        output_lines.append(sub_line)
                        i += 1
            elif re.match(r'^### |^## ', next_line):
                # Hit another section heading, break out
                break
            else:
                output_lines.append(next_line)
                i += 1
    else:
        output_lines.append(line)
        i += 1

# Write the output
with open('Article_30_Development_Review_Procedures.md', 'w', encoding='utf-8') as f:
    f.write('\n'.join(output_lines))

print("Fixed heading hierarchy in Article 30")
