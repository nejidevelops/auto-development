#!/bin/bash

# Set the directory containing your .mpeg files
DIRECTORY="$HOME/Downloads"

# Check if the directory exists
if [[ ! -d "$DIRECTORY" ]]; then
    echo "Error: The directory '$DIRECTORY' does not exist."
    exit 1
fi

echo "Directory '$DIRECTORY' found. Checking files..."

# Step 1: Identify and delete duplicate files
declare -A base_filenames

echo "Identifying and deleting duplicate files (if any)..."
for filepath in "$DIRECTORY"/whatsapp*.mpeg; do
    # Check if the file exists to avoid processing non-existent files
    if [[ -f "$filepath" ]]; then
        filename=$(basename "$filepath")
        echo "Found file: $filename"  # Print all found files for visibility

        # Extract the base filename (e.g., remove "(1)" and ".mpeg" from "whatsapp (1).mpeg")
        base_name="${filename%% *}"  # Get the base name without duplicates

        if [[ -n "${base_filenames[$base_name]}" ]]; then
            echo "Deleting duplicate file: $filename"
            rm "$filepath"
        else
            base_filenames["$base_name"]="$filepath"
        fi
    fi
done

echo "Duplicate deletion completed!"

# Step 2: Convert remaining .mpeg files to .mp3
echo "Starting conversion of remaining .mpeg files to .mp3 format..."
for filepath in "${base_filenames[@]}"; do
    output_file="${filepath%.mpeg}.mp3"

    # Use ffmpeg to convert the file to .mp3 format
    echo "Converting $filepath to $output_file..."
    ffmpeg -i "$filepath" "$output_file" -y

    if [[ $? -eq 0 ]]; then
        echo "Successfully converted to .mp3 format."
    else
        echo "Failed to convert $filepath."
    fi
done

echo "Conversion process completed!"
