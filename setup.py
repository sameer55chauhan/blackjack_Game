from cx_Freeze import setup, Executable
import sys
import os


base = 'Win32GUI' if sys.platform=='win32' else None

PYTHON_INSTALL_DIR = os.path.dirname(os.path.dirname(os.__file__))
os.environ['TCL_LIBRARY'] = os.path.join(PYTHON_INSTALL_DIR, 'tcl', 'tcl8.6')
os.environ['TK_LIBRARY'] = os.path.join(PYTHON_INSTALL_DIR, 'tcl', 'tk8.6')

options = {
    'build_exe': {
        'include_files':[
            os.path.join(PYTHON_INSTALL_DIR, 'DLLs', 'tk86t.dll'),
            os.path.join(PYTHON_INSTALL_DIR, 'DLLs', 'tcl86t.dll'),
        ],
    },
}

executables = [
    Executable('bj.py', base=base)
]

setup(name='Blackjack_Game_GUI',
      version='2.0',
      description='Blackjack a casino game',
      options=options,
      executables=executables)
