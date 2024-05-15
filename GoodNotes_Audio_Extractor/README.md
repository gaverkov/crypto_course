# GoodNotes Audio Extractor 🎧

Welcome to the [GoodNotes Audio Extractor repository](https://github.com/hoseinpur/GoodNotes_Audio_Extractor)! This Python script is designed to help you extract audio files from GoodNotes documents quickly and efficiently.

## How it Works

The GoodNotes Audio Extractor script parses GoodNotes files (with a .goodnotes extension) and extracts audio files embedded within them. Once audio files are identified, the script renames the audio files based on their creation date and moves them to a specified output directory.

## Requirements

To run the GoodNotes Audio Extractor script, you'll need:

- Python 3.x installed on your system
- GoodNotes files (.goodnotes) containing embedded audio files

## Usage

1. Clone this repository to your local machine or download the script file directly.
2. Ensure you have Python 3.x installed.
3. Place your GoodNotes files (.goodnotes) in the same directory as the script.
4. Run the script using the command `python3 GoodNotes_Audio_Extractor.py`.
5. The extracted audio files will be saved in a new directory with the same name as the GoodNotes file, suffixed with "_Extracted_Audio_Files".

## What to Consider

- Make sure your GoodNotes files contain audio files embedded within them.
- The script will only extract audio files that meet a certain size threshold (in MB).
- If a GoodNotes file does not contain any audio files, the output directory will be empty for it.
- Ensure you have sufficient disk space to store the extracted audio files.

## Contact

If you have any suggestions, feedback, or encounter any issues with the script, please feel free to contact me or create an issue in this repository.


