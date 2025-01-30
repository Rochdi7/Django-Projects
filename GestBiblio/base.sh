#!/bin/bash
# Script to automate commits with 10 unique messages for GestionBibliotheque

# Number of iterations
ITERATIONS=2

# Create a dummy file to modify
FILE_NAME="dummy.txt"

# Array of 10 short commit messages
COMMIT_MESSAGES=(
    "Ajout Livre"
    "Update modèle"
    "Fix bug"
    "Ajout Auteur"
    "Refacto code"
    "Update DB"
    "Ajout Emprunt"
    "Fix relations"
    "Ajout UI"
    "Finalisation"
)

# Check if the file exists, else create it
if [ ! -f "$FILE_NAME" ]; then
    echo "Init file" > "$FILE_NAME"
    git add "$FILE_NAME"
    git commit -m "Init repo"
    echo "Initialized $FILE_NAME and made the first commit."
fi

# Loop to add commits with random messages
for ((i=1; i<=ITERATIONS; i++))
do
    # Pick a random commit message
    RANDOM_INDEX=$((RANDOM % ${#COMMIT_MESSAGES[@]}))
    COMMIT_MESSAGE="${COMMIT_MESSAGES[$RANDOM_INDEX]}"

    # Modify the dummy file
    echo "$COMMIT_MESSAGE - Iter $i" >> "$FILE_NAME"

    # Stage and commit
    git add "$FILE_NAME"
    git commit -m "$COMMIT_MESSAGE"

    echo "Created commit: $COMMIT_MESSAGE"
done

# Push changes
git push origin main

echo "All $ITERATIONS commits have been pushed."
