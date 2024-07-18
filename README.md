Here's a cleaned and formatted version of your `README.md` file for publishing on GitHub:

---

# GeminiWave Unrar

GeminiWave Unrar is a simple Python script to extract RAR and ZIP files using a GUI file dialog. This project includes everything you need to package the script into an executable and create a desktop shortcut.

## Features
- Extract RAR and ZIP files
- Simple GUI for selecting archive files and extraction directory
- Easy setup and packaging into an executable
- Script for creating a desktop shortcut

## Installation

### Prerequisites
- Python (version 3.8 or higher)
- Conda (for environment management)
- `unrar` (command-line tool)

### Setting Up the Environment

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/GeminiWave_unrar.git
    cd GeminiWave_unrar
    ```

2. Create the Conda environment:
    ```bash
    conda env create -f environment.yml
    ```

3. Activate the environment:
    ```bash
    conda activate geminiwave_unrar
    ```

### Creating the Executable

4. Install `pyinstaller` and `pywin32`:
    ```bash
    pip install pyinstaller pywin32
    ```

5. Generate the executable:
    ```bash
    pyinstaller --onefile --noconsole --name GeminiWave_unrar GeminiWave_unrar.py
    ```

### Creating the Desktop Shortcut

6. Run the shortcut creation script:
    ```bash
    python create_shortcut.py
    ```

    This will create a shortcut named "GeminiWave Unrar" on your desktop that points to the executable.

## Usage

- Run the script to select an archive file (RAR or ZIP) and a directory to extract the files:
    ```bash
    python GeminiWave_unrar.py
    ```

- If you have created the executable and shortcut, you can simply use the shortcut to run the application.

## Contributing

1. Fork the repository.
2. Create a new branch:
    ```bash
    git checkout -b feature/your-feature-name
    ```
3. Make your changes and commit them:
    ```bash
    git commit -m "Add some feature"
    ```
4. Push to the branch:
    ```bash
    git push origin feature/your-feature-name
    ```
5. Create a pull request.

## Support

If you find this project useful, please consider supporting me. Your support is greatly appreciated!

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Example Project Structure

```
GeminiWave_unrar/
├── GeminiWave_unrar.py
├── create_shortcut.py
├── environment.yml
├── dist/
│   └── GeminiWave_unrar.exe
├── LICENSE
└── README.md
```

### Explanation of Files
- **GeminiWave_unrar.py**: The main script for extracting RAR and ZIP files.
- **create_shortcut.py**: A script to create a desktop shortcut for the executable.
- **environment.yml**: Conda environment configuration file.
- **dist/**: Directory where the executable will be placed after running PyInstaller.
- **LICENSE**: The license for the project (optional, but recommended).
- **README.md**: This file, providing all the instructions and details about the project.

By following the instructions in the README.md file, users can set up the project environment, create the executable, and generate a desktop shortcut for easy access. If you need further assistance, feel free to ask!
