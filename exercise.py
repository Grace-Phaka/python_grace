import json
chemin = "D:\learningPython\grace.json"
with open("grace.json", "r") as f:
    ajouter = json.load(f)
ajouter.append(20)
with open ("grace.json", "w") as f:
    json.dump(ajouter, f, indent=2)
   
   
    
