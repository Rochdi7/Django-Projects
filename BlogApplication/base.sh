#!/bin/bash
# Script to automate commits with 10 unique messages tailored for Blog Cuisine

# Number of iterations
ITERATIONS=10

# Create a dummy file to modify
FILE_NAME="dummy.txt"

# Array of 10 unique commit messages for the Blog Cuisine project
COMMIT_MESSAGES=(
    "Add Moroccan recipes section"
    "Fix bug in recipe pagination"
    "Update styling for recipe cards"
    "Optimize image loading for articles"
    "Implement search functionality"
    "Enhance user authentication system"
    "Add filtering by recipe categories"
    "Improve accessibility for screen readers"
    "Add related articles section"
    "Fix alignment issue on mobile view"
)

# Check if the file exists, else create it
if [ ! -f "$FILE_NAME" ]; then
    echo "Initializing dummy file" > "$FILE_NAME"
    git add "$FILE_NAME"
    git commit -m "Initial commit with dummy file"
    echo "Initialized $FILE_NAME and made the first commit."
fi

# Loop to add 10 iterations of commits with random messages
for ((i=1; i<=ITERATIONS; i++))
do
    # Pick a random commit message from the array
    RANDOM_INDEX=$((RANDOM % ${#COMMIT_MESSAGES[@]}))
    COMMIT_MESSAGE="${COMMIT_MESSAGES[$RANDOM_INDEX]}"

    # Modify the dummy file
    echo "$COMMIT_MESSAGE - Iteration $i" >> "$FILE_NAME"

    # Stage and commit the changes
    git add "$FILE_NAME"
    git commit -m "$COMMIT_MESSAGE"

    # Output a message for each commit
    echo "Created commit: $COMMIT_MESSAGE"
done

# Push changes to GitHub
git push origin main

echo "All $ITERATIONS commits have been pushed to GitHub."
