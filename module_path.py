from pathlib import Path
# p = Path("D:\learningPython\main.py")
# print(p.name)
# print(p.parent)
# print(p.stem)
# print(p.suffix)
# print(p.parts)
# print(p.exists())
# print(p.is_dir())
# print(p.is_file())
Path.home().iterdir()
gr = [f for f in Path.home().iterdir() if f.is_dir()]
print(gr)


    
    






















