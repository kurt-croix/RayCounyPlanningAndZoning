# AI Editing Instructions for This Workspace

## CRITICAL: Do NOT Use insert_edit_into_file Tool

**The insert_edit_into_file tool has been known to wipe out entire file contents in this workspace.**

### Correct Editing Procedure

1. Read the file first using read_file to understand its current content
2. Use bash commands to make edits instead of insert_edit_into_file
3. Auto-save and commit after each edit
4. Verify the edit by checking line count
5. Rollback if needed if the file was accidentally wiped

### Step-by-Step Process

#### Step 1: Make the edit using bash commands
Example: Adding content to the top of a file
cd "c:\Users\KurtBognar\Downloads\RayCountyZoning"
(echo "new content"; echo ""; cat filename.md) > temp.md && mv temp.md filename.md

Example: Using sed to replace content
sed -i 's/old text/new text/g' filename.md

#### Step 2: Add and commit the changes
cd "c:\Users\KurtBognar\Downloads\RayCountyZoning"
git add filename.md
git commit -m "Description of changes"

#### Step 3: Verify the edit did not wipe the file
cd "c:\Users\KurtBognar\Downloads\RayCountyZoning"
wc -l filename.md

If the line count is less than 10 lines (and it should not be), the file was likely wiped!

#### Step 4: Rollback if the file was wiped
cd "c:\Users\KurtBognar\Downloads\RayCountyZoning"
git reset --hard HEAD~1

### Example Complete Edit Workflow

# 1. Make the edit
cd "c:\Users\KurtBognar\Downloads\RayCountyZoning"
(echo "hello world"; echo ""; cat Article_40_Base_Zoning_Districts.md) > temp.md && mv temp.md Article_40_Base_Zoning_Districts.md

# 2. Commit the change
git add Article_40_Base_Zoning_Districts.md
git commit -m "Add hello world to top of Article 40"

# 3. Verify line count
wc -l Article_40_Base_Zoning_Districts.md

# 4. If line count is suspiciously low (< 10), rollback
git reset --hard HEAD~1

## Why This Approach?

- The insert_edit_into_file tool does not properly preserve existing content
- Bash/shell commands are more reliable for text file manipulation
- Git commits allow easy rollback if something goes wrong
- Line count verification catches accidental file wipes immediately

## User Preferences

- Auto-keep changes: Yes, always save changes automatically
- Commit after edits: Yes, commit each significant change
- Never push: Do not push commits unless explicitly asked
- Verify edits: Always check line count after editing

## File Context

Most markdown files in this workspace are large (400-600+ lines). If a file shows < 10 lines after editing, it was almost certainly wiped accidentally.

Expected Line Counts (Approximate):
- Article_10: 50-100 lines
- Article_20: 50-100 lines  
- Article_30: 400-600 lines
- Article_40: 600-800 lines
- Article_60: 400-600 lines
- Article_80: 300-500 lines

Always compare post-edit line count with these expectations!
