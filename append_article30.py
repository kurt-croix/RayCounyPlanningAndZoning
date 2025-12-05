#!/usr/bin/env python3
"""
Append missing Article 30 sections to the markdown file
"""

# Read lines 1290-2733 from the txt file
with open('C:/Users/KurtBognar/Downloads/RayCountyZoning/RAY COUNTY PLANNING & ZONING 2005.doc.txt', 
          'r', encoding='utf-8', errors='ignore') as f:
    lines = f.readlines()

# Eract the needed section (0-indexed: lines[1289:2734])
content = ''.join(lines[1289:2734])

# Save the raw extracted content for review
with open('C:/Users/KurtBognar/Downloads/RayCountyZoning/article30_extracted_raw.txt', 
          'w', encoding='utf-8') as f:
    f.write(content)

print("Extracted lines 1290-2734 from txt file")
print(f"Total characters: {len(content)}")
print("\nFirst 500 characters:")
print(content[:500])
print("\n\nContent saved to: article30_extracted_raw.txt")
print("\nPlease review e to create the proper markdown formatting.")
