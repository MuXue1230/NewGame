import os

from snowskystudio.newgame.test.Logger import Logger

logger = Logger("Builder")

logger.info("Building begins.")

logger.info("Clearing folder build...")
os.system("powershell -command Remove-Item build/* -r")
logger.info("Copying Files")
logger.debug("> Main scripts")
os.system("powershell -command Copy-Item cn build/cn -r")
logger.debug("> Game assets")
os.system("powershell -command Copy-Item assets build/assets -r")
logger.debug("> Virtual Environment")
os.system("powershell -command Copy-Item .venv build/.GVE -r")
logger.debug("> Launcher scripts")
os.system("powershell -command Copy-Item launch.py build/launch.py")
logger.info("Writing Launcher")
with open("build/Launcher.ps1", 'w') as launcher_file:
    launcher_file.write(".\\.GVE\\Scripts\\Activate.ps1\n")
    launcher_file.write(".\\launch.py\n")

logger.info("Finished building.")
