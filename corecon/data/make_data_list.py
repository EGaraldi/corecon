import os

exclude_dirs = []

with open("data.yaml", "w") as datafile:

    for d in os.listdir('.'):
        if os.path.isdir(d) and not (d in exclude_dirs):
    
            datafile.write(f"{d}:\n")

            for f in os.listdir(d):
                if f != "__init__.py":
                    datafile.write(f"  - {f}\n")
            
            datafile.write("\n")
