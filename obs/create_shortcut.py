import os
import sys
from pathlib import Path

def create_shortcut(target, shortcut_name, icon=None):
    desktop = Path.home() / "Desktop"
    shortcut_path = desktop / f"{shortcut_name}.lnk"

    # Windows only
    import pythoncom
    import win32com.client

    shell = win32com.client.Dispatch("WScript.Shell")
    shortcut = shell.CreateShortCut(str(shortcut_path))
    shortcut.Targetpath = target
    shortcut.WorkingDirectory = os.path.dirname(target)
    if icon:
        shortcut.IconLocation = icon
    shortcut.save()

if __name__ == "__main__":
    # Path to the executable
    exec_path = Path(__file__).parent / "dist" / "GeminiWave_unrar.exe"

    # Shortcut name
    shortcut_name = "GeminiWave Unrar"

    # Optional: Path to the icon (must be .ico file)
    icon_path = None

    create_shortcut(exec_path, shortcut_name, icon_path)
