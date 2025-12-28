import subprocess, datetime
from datetime import *

now = datetime.now().time()
today = date.today()

#4mat
version = f"{today.year + today.month + today.day}.{now.hour + now.minute}"
print(version)

# git tag _
# git push origin --tags
commitfirst = subprocess.run(["git", "push"], capture_output=True, text=True)
maketag = subprocess.run(["git", "tag", version], capture_output=True, text=True)
pushtag = subprocess.run(["git", "push", "origin" "--tags"], capture_output=True, text=True)