import cx_Freeze
import sys
import os
base = None

if sys.platform == 'win32':
    base = "Win32GUI"

os.environ['TCL_LIBRARY'] = r"C:\Users\abhay\AppData\Local\Programs\Python\Python39\tcl\tcl8.6"
os.environ['TK_LIBRARY'] = r"C:\Users\abhay\AppData\Local\Programs\Python\Python39\tcl\tk8.6 "

executables = [cx_Freeze.Executable("Face_Recognition_Software.py", base=base, icon="explorationoffacerecognition_facescanning_exploraciondereconocimientoderostro_4589.ico")]

cx_Freeze.setup(
    name="Face Recognition Software",
    options={"build_exe": {"packages": ["tkinter", "os"],
                           "include_files": ["explorationoffacerecognition_facescanning_exploraciondereconocimientoderostro_4589.ico", 'tcl86t.dll', 'tk86t.dll', 'images',
                                             'Data','Database', 'AttendanceReport']}},
    version="1.0",
    description="Face Recognition Automatic Attendace System | Developed By Abhay Maurya",
    executables=executables
)
