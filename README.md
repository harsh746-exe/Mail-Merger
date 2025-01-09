# Personalized Letter Generator

This Python script automates the creation of personalized letters by replacing placeholder text in a template letter with names from a provided list. The resulting letters are saved as individual files, ready to be sent.

---

## How It Works

1. **Input Files**:
   - `./Input/Names/invited_names.txt`: Contains a list of names, each on a new line.
   - `./Input/letters/starting_letter.txt`: A template letter containing a placeholder `[name]` where the names will be inserted.

2. **Output**:
   - Personalized letters are saved in the `./Output/ReadyToSend/` directory, with filenames in the format `letter_for_<name>.txt`.

3. **Process**:
   - The script reads names from `invited_names.txt`.
   - It iterates through each name, replacing the `[name]` placeholder in the template with the actual name.
   - The customized letter is saved as a new file in the `ReadyToSend` directory.

---

## Prerequisites

- Python 3 installed on your system.
- Ensure the file paths and directory structure match the script:
  ```
  .
  ├── Input
  │   ├── Names
  │   │   └── invited_names.txt
  │   └── letters
  │       └── starting_letter.txt
  └── Output
      └── ReadyToSend
  ```

---

## Usage

1. Place the list of names in `invited_names.txt`.
2. Write your template letter in `starting_letter.txt` and include `[name]` as a placeholder where each name should appear.
3. Run the script:
   ```bash
   python script.py
   ```
4. Check the `./Output/ReadyToSend/` directory for the personalized letters.
