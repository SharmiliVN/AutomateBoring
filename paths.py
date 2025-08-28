from pathlib import Path

import os

print(Path.cwd())

os.chdir('C:\\Windows\\System32')

print(Path.cwd())
print(Path.home())

from pathlib import Path
win_dir = Path('C:/Windows')
not_exixts_dir = Path('C:/This/Folder/Does/Not/Exist')
calc_file_path = Path('C:/Windows/System32/calc.exe')
print(win_dir.exists())

p = Path('spam.txt')
print(p.write_text('hello world!'))
print(p.read_text())

from pathlib import Path
hello_file = open(Path.home() / 'hello.txt', encoding = 'UTF-8')
