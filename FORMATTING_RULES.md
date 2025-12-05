# Markdown Formatting Rules for Ray County Zoning Documents

## Overview
These rules were developed to fix inconsistent formatting in the Ray County Zoning Regulations markdown files, particularly Article 30 (Development Review Procedures).

## Heading Hierarchy Rules

### 1. Convert Bold Numbered/Lettered Items to Proper Headings
When bold numbered or lettered items appear under a heading and describe subsections (not simple list items):

- **Under `###` headings**: Convert `**1. Title**` → `#### 1. Title`
- **Under `####` headings**: Convert `**a. Title**` → `##### a. Title`
- **Pattern**: Bold list markers followed by descriptive text should become headings at the next level down

**Example:**
```markdown
### C. Fees

**1. Application Filing Fees**
Applications must be accompanied by...

**2. Special Hearing Deposit**
Where the total time...
```

**Should become:**
```markdown
### C. Fees

#### 1. Application Filing Fees
Applications must be accompanied by...

#### 2. Special Hearing Deposit
Where the total time...
```

### 2. Keep Plain List Items as Plain Text
Keep as plain text when items are:
- Simple enumerated criteria (1, 2, 3...)
- Sub-items under headings that are truly list content, not subsections
- Short criteria or requirements without detailed explanations

**Example (keep as plain list):**
```markdown
#### 4. Sign Plan Approval Criteria

A Sign Plan may be approved only if:

1. the Sign Plan complies with all applicable standards;
2. the Sign Plan is consistent with any approved PUD;
```

## Spacing and Consistency Rules

### 3. Normalize Spacing
- **Remove excessive whitespace** in headings (multiple spaces → single space)
  - `###  Heading` → `### Heading`
  - `### A.        Title` → `### A. Title`
- **Remove trailing spaces** from headings
- **Ensure consistent spacing** between sections

### 4. Fix Mixed List Formatting
When items under a heading mix styles inconsistently:
- If mixing "1." as plain text with "b." with excessive spacing
- Convert to consistent numbered list (1, 2, 3...)
- Remove arbitrary spacing between list markers and text

**Example of incoherent formatting:**
```markdown
#### 4. Approval Criteria

1. the criterion complies with standards


b.        the criterion is consistent with plans
```

**Should become:**
```markdown
#### 4. Approval Criteria

1. the criterion complies with standards
2. the criterion is consistent with plans
```

## When to Apply These Rules

Apply these rules when:
1. **Inconsistent hierarchy** - Some subsections use bold formatting while sibling subsections use proper heading markers
2. **Spacing is incoherent** - Excessive spaces, inconsistent indentation
3. **Mixed list styles** - Numbered items appear as both headings and plain text in the same context
4. **Navigation is broken** - Document outline/TOC doesn't properly reflect structure

## Goal

Create a **consistent, navigable document structure** where:
- Headings properly reflect the document's organizational hierarchy
- Similar content uses similar formatting
- The document outline clearly shows the structure
- Spacing is clean and professional

## Hierarchy Pattern Summary

```
# Article Title
## Major Section (30.1, 30.2, etc.)
### Lettered Subsection (A, B, C)
#### Numbered Subsection (1, 2, 3)
##### Lettered Sub-subsection (a, b, c)
```

For lists vs. headings:
- Use **headings** (`####`, `#####`) when the item has a title and substantial content below it
- Use **plain lists** when items are simple criteria, requirements, or brief points

## Common Patterns to Fix

1. `**1. Title**` under `###` → Convert to `#### 1. Title`
2. `**a. Title**` under `####` → Convert to `##### a. Title`
3. Multiple spaces in headings → Single space
4. Inconsistent list numbering (1, b, 3) → Consistent numbering (1, 2, 3)
5. Excessive spacing before text in lists → Normal spacing

## Tools Used

These fixes were applied using Python scripts that:
1. Read the markdown file line by line
2. Detect bold patterns followed by numbered/lettered content
3. Convert to appropriate heading level based on context
4. Normalize spacing throughout
5. Preserve actual list items that should remain as lists

## Notes

- These rules prioritize **semantic correctness** over visual appearance
- Proper heading hierarchy enables better navigation in markdown viewers and documentation tools
- Consistency makes the document easier to maintain and update
- The rules can be applied to other articles in the Ray County Zoning Regulations using similar patterns
