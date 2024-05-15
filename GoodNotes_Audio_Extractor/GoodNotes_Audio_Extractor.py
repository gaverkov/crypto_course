#!/usr/bin/env python3

import os
import zipfile
import shutil
from datetime import datetime

def parse_prefix(line, fmt):
    '''
    Parses the prefix from a line with the specified format.
    
    Returns:
        str: The parsed prefix.
    '''
    try:
        t = datetime.strptime(line, fmt)
    except ValueError as v:
        if len(v.args) > 0 and v.args[0].startswith('unconverted data remains: '):
            line = line[:-(len(v.args[0]) - 26)]
            t = datetime.strptime(line, fmt)
        else:
            raise
    return t.strftime('%m-%d_%H-%M')

def extract_voice_files(goodnotes_file, output_dir):
    '''
    Extracts audio files from a GoodNotes file and renames them.
    
    Returns:
        output_dir (str): The directory to save the extracted audio files.
    '''
    # Create output directory if it doesn't exist
    os.makedirs(output_dir, exist_ok=True)

    try:
        # Open the GoodNotes file as a ZIP archive
        with zipfile.ZipFile(goodnotes_file, 'r') as zip_ref:
            # Extract all files from the ZIP archive to a temporary directory
            temp_dir = os.path.join(output_dir, "temp")
            zip_ref.extractall(temp_dir)

            # Check if "attachments" folder exists in the extracted directory
            attachments_dir = os.path.join(temp_dir, "attachments")
            if os.path.exists(attachments_dir):
                # List audio files in the attachments directory
                audio_files = [file for file in os.listdir(attachments_dir) if os.path.isfile(os.path.join(attachments_dir, file))]

                # Filter audio files that are in MB size
                audio_files = [file for file in audio_files if os.path.getsize(os.path.join(attachments_dir, file)) > 1024 * 1024]
                
                # Sort audio files based on creation time
                audio_files.sort(key=lambda x: os.path.getctime(os.path.join(attachments_dir, x)))

                # Initialize audio count for renaming
                audio_count = 0

                # Rename and move the audio files to the output directory
                for file in audio_files:
                    audio_count += 1
                    # Get file creation date for renaming
                    creation_time = os.path.getctime(os.path.join(attachments_dir, file))
                    # Format creation time as a string
                    creation_time_str = datetime.fromtimestamp(creation_time).strftime('%Y%m%d%H%M%S')
                    # Construct new file name
                    new_filename = f"Audio_{audio_count}.mp4"
                    # Move the audio file to the output directory
                    shutil.move(os.path.join(attachments_dir, file), os.path.join(output_dir, new_filename))
                    print(f"Renamed and moved audio file: {new_filename}")

                # Print the total number of audio files extracted
                print(f"Total {audio_count} audio file(s) extracted successfully.")

            # Remove the temporary directory
            shutil.rmtree(temp_dir)

    except zipfile.BadZipFile:
        print("Error: Not a valid GoodNotes file.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    # Get the list of all files in the current directory
    files_in_dir = os.listdir()

    # Iterate over each file in the directory
    for file in files_in_dir:
        # Check if the file is a GoodNotes file (ends with .goodnotes)
        if file.endswith('.goodnotes'):
            # Create output directory for each GoodNotes file
            output_dir = os.path.splitext(file)[0] + "_Extracted_Audio_Files"
            
            # Extract voice files from GoodNotes file
            extract_voice_files(file, output_dir)
