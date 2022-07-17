import os
import zipfile
import subprocess

exclude_dirs = []

with zipfile.ZipFile("data.zip", "w") as zipfile:

    for d in os.listdir('.'):
        if os.path.isdir(d) and not (d in exclude_dirs):
            for f in os.listdir(d):
                if f != "__init__.py":
                    zipfile.write(os.path.join(d,f))


process = subprocess.Popen(['git', 'add', 'data.zip']            , stdout=subprocess.PIPE, stderr=subprocess.PIPE)
process = subprocess.Popen(['git', 'commit', '-m "updated data"'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
process = subprocess.Popen(['git', 'push']                       , stdout=subprocess.PIPE, stderr=subprocess.PIPE)
