import os
import sys
import rarfile
import zipfile
from tkinter import Tk
from tkinter.filedialog import askdirectory, askopenfilename

def select_archive_file():
    """Open a dialog to select a RAR or ZIP file."""
    Tk().withdraw()  # We don't want a full GUI, so keep the root window from appearing
    archive_file_path = askopenfilename(filetypes=[("Archive files", "*.rar *.zip")])
    return archive_file_path

def select_extract_path():
    """Open a dialog to select a directory to extract files."""
    Tk().withdraw()  # We don't want a full GUI, so keep the root window from appearing
    extract_path = askdirectory()
    return extract_path

def extract_rar(rar_file_path, extract_path):
    """Extract a RAR file using the `rarfile` library with progress and error handling."""
    try:
        with rarfile.RarFile(rar_file_path) as rf:
            total_files = len(rf.infolist())
            print(f"Extracting {total_files} files from RAR...")
            for i, member in enumerate(rf.infolist(), 1):
                rf.extract(member, extract_path)
                print(f"Extracted {i}/{total_files} files", end='\r')
        print("\nRAR Extraction successful.")
    except rarfile.Error as e:
        print(f"An error occurred: {e}")

def extract_zip(zip_file_path, extract_path):
    """Extract a ZIP file using the `zipfile` library with progress and error handling."""
    try:
        with zipfile.ZipFile(zip_file_path, 'r') as zf:
            total_files = len(zf.infolist())
            print(f"Extracting {total_files} files from ZIP...")
            for i, member in enumerate(zf.infolist(), 1):
                zf.extract(member, extract_path)
                print(f"Extracted {i}/{total_files} files", end='\r')
        print("\nZIP Extraction successful.")
    except zipfile.BadZipFile as e:
        print(f"An error occurred: {e}")

def main():
    # Open file dialog to select RAR or ZIP file
    archive_file_path = select_archive_file()
    if not archive_file_path:
        print("No archive file selected.")
        return

    # Open directory dialog to select extraction path
    extract_path = select_extract_path()
    if not extract_path:
        print("No extraction directory selected.")
        return

    # Determine file type and extract accordingly
    if archive_file_path.lower().endswith('.rar'):
        extract_rar(archive_file_path, extract_path)
    elif archive_file_path.lower().endswith('.zip'):
        extract_zip(archive_file_path, extract_path)
    else:
        print("Unsupported file type.")

if __name__ == "__main__":
    main()
