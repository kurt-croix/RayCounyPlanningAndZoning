#!/usr/bin/env python3
import re

with open('C:/Users/KurtBognar/Downloads/RayCountyZoning/Article_30_Development_Review_Procedures.md', 'r', encoding='utf-8') as f:
    content = f.read()

# Fix 1: Parenthetical numbered items on same line as text
# Pattern: "text: (1) item; (2) item; and (3) item."
# Should be: "text:\n\n   1. item\n   2. item\n   3. item"
def fix_inline_numbered_lists(text):
    # Pattern: ends with colon, then has (1), (2), (3) items
    pattern = r'([^\n]+:)\s*\(1\)([^;]+);?\s*\(2\)([^;]+);?\s*(?:and\s*)?\(3\)([^.]+)\.'
    
    def replace_func(match):
        intro = match.group(1)
        item1 = match.group(2).strip()
        item2 = match.group(3).strip()
        item3 = match.group(4).strip()
        return f'{intro}\n\n1. {item1}\n2. {item2}\n3. {item3}'
    
    text = re.sub(pattern, replace_func, text)
    
    # Also handle (1), (2), (3), (4) patterns
    patterr'([^\n]+:)\s*\(1\)([^;]+);?\s*\(2\)([^;]+);?\s*\(3\)([^;]+);?\s*(?:and\s*)?\(4\)([^.]+)\.'
    
    def replace_func4(match):
        intro = match.group(1)
        item1 = match.group(2).strip()
        item2 = match.group(3).strip()
        item3 = match.group(4).strip()
        item4 = match.group(5).strip()
        return f'{intro}\n\n1. {item1}\n2. {item2}\n3. {item3}\n4. {item4}'
    
    text = re.sub(pattern4, replace_func4, text)
    
    return text

# Fix 2: It i spanning multiple lines (section 30.4 A i)
# Pattern: "i.    Text\nmore text\nmore text."
def fix_multi_line_items(text):
    # Find the specific problem with item i in 30.4 A
    text = re.sub(
        r'i\.\s+A division of property through the probate of an estate, or by\s+order or judgment of a court of law of competent jurisdiction of the State of\s+Missouri\.',
        'i. A division of property through the probate of an estate, or by order or judgment of a court of law of competent jurisdiction of the State ouri.',
        text
    )
    return text

# Fix 3: Remove excessive blank lines (already mostly done, but double-check)
def fix_blank_lines(text):
    # Max 2 consecutive blank lines
    text = re.sub(r'\n{4,}', '\n\n\n', text)
    return text

# Fix 4: Fix items 1, 2 that got made bold when they shouldn't be (in section 30.F)
# These are list items, not headers
def fix_over_bolded_items(text):
    # In section F, items 1, 2, 3, 4, 5 should not be bold
    text = re.sub(
        r'\*\*1\. Deadlines for receipt of complete applicat*',
        '1. Deadlines for receipt of complete applications;',
        text
    )
    text = re.sub(
        r'\*\*2\. Dates of regular meetings;\*\*',
        '2. Dates of regular meetings;',
        text
    )
    return text

# Apply all fixes
content = fix_inline_numbered_lists(content)
content = fix_multi_line_items(content)
content = fix_blank_lines(content)
content = fix_over_bolded_items(content)

# Write back
with open('C:/Users/KurtBognar/Ds/RayCountyZoning/Article_30_Development_Review_Procedures.md', 'w', encoding='utf-8') as f:
    f.write(content)

print("✓ Fixed inline numbered lists - moved (1), (2), (3) to separate lines")
print("✓ Fixed multi-line item i in section 30.4 A")
print("✓ Fixed excessive blank lines")
print("✓ Fixed over-bolded list items")
print("\nDone!")
