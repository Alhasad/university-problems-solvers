import cx_Freeze
from cx_Freeze import *

setup(
    name = "principal",
    # options = {'build_exe': {'packages': ['']}},
    executables=[
        Executable(
            "principal.py",

            )
        
        ]
    )
