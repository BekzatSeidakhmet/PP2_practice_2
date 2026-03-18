import shutil

shutil.copy("example.txt", "backup.txt")

import os

if os.path.exists("backup.txt"):
    os.remove("backup.txt")