import sys
from cx_Freeze import setup,Executable

# Dependencies are automatically detected, but it might need fine tuning.
build_exe_options = {"packages": ["os"]}
includefiles =['garment.db','bill.docx','icon.ico','logo.png','qr.png','report.docx']

target = Executable(
    script="front.py",
    base="Win32GUI",
    icon = "icon.ico"
    )
# GUI applications require a different base on Windows (the default is for a
# console application).
base = None
if sys.platform == "win32":
    base = "Win32GUI"

setup(  name = "Al mansoor garments",
        version = "0.1 BETA",
        description = "A product of fluff coders limited ",
        options = {"build_exe": {"packages": ["os"], "include_files":includefiles}},
        executables=[target])
