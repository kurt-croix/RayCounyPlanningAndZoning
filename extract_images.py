import base64
import re

# Read the markdown file
with open('c:/Users/KurtBognar/Downloads/MarkdownFile.md', 'r', encoding='utf-8') as f:
    content = f.read()

# Find all base64 image data
pattern = r'!\[\]\(data:image/png;base64,([^)]+)\)'
matches = re.findall(pattern, content)

print(f'Found {len(matches)} embedded images')

# Extract and save all images
for i, base64_data in enumerate(matches):
    try:
        # Decode the base64 data
        image_data = base64.b64decode(base64_data)
        
        # Save as PNG file with descriptive names
        filename = f'images/diagram_{i+1:02d}.png'
        with open(filename, 'wb') as f:
            f.write(image_data)
        
        print(f'Extracted: {filename} ({len(image_data)} bytes)')
    except Exception as e:
        print(f'Error with image {i+1}: {e}')

print('\nAll images extracted successfully!')

# Now create a new markdown file with image references instead of embedded data
print('\nCreating new markdown with image references...')

# Replace embedded images with file references
new_content = content
image_counter = 1

for match in re.finditer(pattern, content):
    embedded_image = match.group(0)
    image_ref = f'![Diagram {image_counter:02d}](images/diagram_{image_counter:02d}.png)'
    new_content = new_content.replace(embedded_image, image_ref, 1)
    image_counter += 1

# Write the new markdown file
with open('MarkdownFile_with_image_refs.md', 'w', encoding='utf-8') as f:
    f.write(new_content)

print('Created: MarkdownFile_with_image_refs.md with proper image references')