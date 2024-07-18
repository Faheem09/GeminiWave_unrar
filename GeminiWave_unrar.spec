# -*- mode: python ; coding: utf-8 -*-

a = Analysis(
    ['GeminiWave_unrar.py'],  # Ensure this matches the name of your updated Python file
    pathex=[],
    binaries=[],
    datas=[],
    hiddenimports=['rarfile', 'zipfile', 'tkinter'],  # Include any libraries not auto-detected
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    optimize=0,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='GeminiWave_unrar',  # Ensure this matches the desired name for your executable
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=True,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
