import re
import os
from pathlib import Path

def apply_formatting_rules(content):
    """Apply formatting rules to markdown content"""
    lines = content.split('\n')
    output = []
    i = 0
    
    while i < len(lines):
        line = lines[i]
        stripped = line.strip()
        
        # Check for bold numbered/lettered items that should be headings
        # Pattern: **1. Title** or **a. Title** etc.
        bold_pattern = re.match(r'^\*\*(([0-9]+|[a-z]|[A-Z])\.?\s+.+?)\*\*\s*$', stripped)
        
        if bold_pattern:
            inner_text = bold_pattern.group(1)
            
            # Determine what heading level this should be based on context
            # Look at previous headings
            heading_level = None
            for j in range(i-1, max(0, i-20), -1):
                prev_line = lines[j].strip()
                if prev_line.startswith('#'):
                    prev_level = len(prev_line) - len(prev_line.lstrip('#'))
                    # Bold items should be one level deeper
                    heading_level = prev_level + 1
                    break
            
            # Default to #### if we can't determine
            if heading_level is None:
                heading_level = 4
            
            # Cap at 6 levels
            heading_level = min(heading_level, 6)
            
            # Convert to heading
            output.append('#' * heading_level + ' ' + inner_text)
        
        # Fix headings with excessive spacing
        elif stripped.startswith('#'):
            # Extract heading markers
            heading_match = re.match(r'^(#{1,6})\s+(.+)$', stripped)
            if heading_match:
                markers = heading_match.group(1)
                text = heading_match.group(2)
                
                # Normalize spacing in the text (multiple spaces to single)
                text = re.sub(r'\s{2,}', ' ', text)
                text = text.strip()
                
                output.append(markers + ' ' + text)
            else:
                output.append(line)
        
        # Keep other lines as-is
        else:
            output.append(line)
        
        i += 1
    
    return '\n'.join(output)

# Get all Article markdown files
article_files = sorted(Path('.').glob('Article_*.md'))

print(f'Found {len(article_files)} Article markdown files')
print('Applying formatting rules...\n')

for file_path in article_files:
    print(f'Processing: {file_path.name}')
    
    try:
        # Read the file
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Apply formatting rules
        formatted_content = apply_formatting_rules(content)
        
        # Write back
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(formatted_content)
        
        print(f'  ✓ Successfully formatted {file_path.name}')
    
    except Exception as e:
        print(f'  ✗ Error processing {file_path.name}: {e}')

print('\nFormatting complete!')
