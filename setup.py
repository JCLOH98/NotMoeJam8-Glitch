import cx_Freeze
from cx_Freeze import *

exe = [Executable("Glitchman TV.py")]

setup(name="Glitchman TV",
      version="",
      description="Glitchman TV created by JCLOH",
      options={"build_exe":{"packages":["pygame"]}},
      executables=exe
      )
