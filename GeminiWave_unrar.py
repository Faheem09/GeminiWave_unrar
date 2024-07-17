import os
import sys
import rarfile
from tkinter import Tk
from tkinter.filedialog import askdirectory

def select_extract_path():
    """Open a dialog to select a directory to extract files."""
    Tk().withdraw()  # We don't want a full GUI, so keep the root window from appearing
    extract_path = askdirectory()
    return extract_path

def extract_rar(rar_file_path, extract_path):
    """Extract a RAR file using the `rarfile` library."""
    with rarfile.RarFile(rar_file_path) as rf:
        rf.extractall(extract_path)
    print("Extraction successful.")

def main():
    # Check if a file path is provided as a command-line argument
    if len(sys.argv) > 1:
        rar_file_path = sys.argv[1]
    else:
        print("No file provided.")
        return

    extract_path = select_extract_path()
    if not extract_path:
        print("No extraction directory selected.")
        return

    extract_rar(rar_file_path, extract_path)

if __name__ == "__main__":
    main()
