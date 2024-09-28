import os
import re
import subprocess

# Set the directory containing your .mpeg files
directory = os.path.expanduser("~/Downloads")

# Check if the directory exists before proceeding
if not os.path.exists(directory):
    print(f"Error: The directory '{directory}' does not exist.")
else:
    print(f"Directory '{directory}' found. Checking files...")

    # Dictionary to keep track of base filenames
    base_filenames = {}

    # Step 1: Identify and delete duplicate files
    print("Identifying and deleting duplicate files (if any)...")
    for filename in os.listdir(directory):
        print(f"Found file: {filename}")  # Print all found files for visibility

        # Check if the file is an mpeg file starting with "whatsapp"
        if filename.startswith("whatsapp") and filename.endswith(".mpeg"):
            # Extract the base filename (e.g., remove "(1)" and ".mpeg" from "whatsapp (1).mpeg")
            base_name_match = re.match(r"^(.*?)( \(\d+\))?\.mpeg$", filename)
            if base_name_match:
                base_name = base_name_match.group(1)
                print(f"Base filename extracted: {base_name}")

                # If we have seen this base name before, delete the duplicate
                if base_name in base_filenames:
                    print(f"Deleting duplicate file: {filename}")
                    os.remove(os.path.join(directory, filename))
                else:
                    base_filenames[base_name] = filename
            else:
                print(f"Pattern not matched for {filename}. Skipping file.")

    print("Duplicate deletion completed!\n")

    # Step 2: Convert remaining .mpeg files to .mp3
    print("Starting conversion of remaining .mpeg files to .mp3 format...")
    for base_filename, filename in base_filenames.items():
        # Define the full path for the input and output files
        input_file = os.path.join(directory, filename)
        output_file = os.path.join(directory, filename.replace(".mpeg", ".mp3"))

        # Check if the input file exists before conversion
        if not os.path.exists(input_file):
            print(f"Error: Input file '{input_file}' not found.")
            continue

        # Use ffmpeg to convert the file to .mp3 format
        command = ["ffmpeg", "-i", input_file, output_file]
        print(f"Converting {input_file} to {output_file} using command: {command}...")

        # Run the command using subprocess
        result = subprocess.run(command, capture_output=True, text=True)

        # Print the result of the conversion
        if result.returncode == 0:
            print(f"Successfully converted {filename} to .mp3 format.")
        else:
            print(f"Failed to convert {filename}. Error:")
            print(result.stderr)  # Display ffmpeg error output

    print("\nConversion process completed!")
