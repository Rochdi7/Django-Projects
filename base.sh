#!/bin/bash
# Script to automate commits

# Number of commits you want to add
NUM_COMMITS=10

# Create a dummy file to modify
FILE_NAME="dummy.txt"

# Check if file exists, else create it
if [ ! -f "$FILE_NAME" ]; then
    echo "Initializing dummy file" > "$FILE_NAME"
    git add "$FILE_NAME"
    git commit -m "Initial commit for automation"
fi

# Loop to add commits
for ((i=1; i<=NUM_COMMITS; i++))
do
    echo "Commit $i" >> "$FILE_NAME"  # Modify the file
    git add "$FILE_NAME"             # Stage changes
    git commit -m "Automated commit $i"  # Create commit
    echo "Created commit $i"
done

# Push changes to GitHub
git push origin main
