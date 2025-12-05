import base64
import re
import os

# Ensure images directory exists
os.makedirs('images', exist_ok=True)

# Read the markdown file using relative path
with open('../MarkdownFile.md', 'r', encoding='utf-8') as f:
    content = f.read()

print("Extracting embedded base64 images...")

# Find all embedded images and extract them
image_counter = 1

# Simple approach: find all occurrences of base64 image data
lines = content.split('\n')
new_lines = []

for i, line in enumerate(lines):
    if 'data:image/png;base64,' in line:
        # Extract the base64 data
        start_idx = line.find('data:image/png;base64,') + len('data:image/png;base64,')
        end_idx = line.find(')', start_idx)
        
        if end_idx != -1:
            base64_data = line[start_idx:end_idx]
            
            try:
                # Decode and save the image
                image_data = base64.b64decode(base64_data)
                filename = f'images/diagram_{image_counter:02d}.png'
                
                with open(filename, 'wb') as img_file:
                    img_file.write(image_data)
                
                print(f"Extracted: {filename} ({len(image_data)} bytes)")
                
                # Replace the embedded image with a reference
                new_line = line.replace(f'![](data:image/png;base64,{base64_data})', f'![Diagram {image_counter:02d}]({filename})')
                new_lines.append(new_line)
                
                image_counter += 1
            except Exception as e:
                print(f"Error processing image on line {i+1}: {e}")
                new_lines.append(line)
        else:
            new_lines.append(line)
    else:
        new_lines.append(line)

# Write the updated content to a new file
updated_content = '\n'.join(new_lines)
with open('MarkdownFile_with_image_refs.md', 'w', encoding='utf-8') as f:
    f.write(updated_content)

print(f"\nSuccessfully extracted {image_counter-1} images and updated the markdown file!")
print("Created: MarkdownFile_with_image_refs.md with proper image references")
print("All embedded base64 images have been converted to proper image files.")