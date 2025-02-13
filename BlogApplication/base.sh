#!/bin/bash
# Script to automate commits after completing the Django project

# Number of iterations
ITERATIONS=10

# Create a dummy file to modify
FILE_NAME="project_test_log.txt"

# Array of 10 short commit messages
COMMIT_MESSAGES=(
    "Project done! Ready for tests."
    "Final tweaks before testing."
    "Preparing for first test run."
    "Fixing last-minute details."
    "Finalizing setup for tests."
    "Reviewing configurations."
    "Ensuring stability before test."
    "Final review before launch."
    "Almost there! Testing next."
    "Final touches. Running tests."
)

# Check if the file exists, else create it
if [ ! -f "$FILE_NAME" ]; then
    echo "Initializing test log file" > "$FILE_NAME"
    git add "$FILE_NAME"
    git commit -m "Initial commit with test log file"
    echo "Initialized $FILE_NAME and made the first commit."
fi

# Loop to add 10 iterations of commits with specific messages
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
git push origin main --force

echo "All $ITERATIONS commits have been pushed to GitHub."
