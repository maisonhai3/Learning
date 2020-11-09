from pathlib import Path
import os

cwd = Path.cwd()
list_filenames = cwd.glob('**/*.jpg')

print(list_filenames)
