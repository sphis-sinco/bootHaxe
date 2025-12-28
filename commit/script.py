import subprocess, datetime, time
from datetime import date
from datetime import datetime

now = datetime.now().time()
today = date.today()

#4mat
version = f"{today.year + today.month + today.day}.{now.hour + now.minute}"
print(version)

# git push
# git tag _
# git push origin --tags

gitpush = subprocess.run(["git", "push"], capture_output=True, text=True)
print(gitpush.stderr)

gittag = subprocess.run(["git", "tag", version], capture_output=True, text=True)
gitpushtag = subprocess.run(["git", "push", "origin", "--tags"], capture_output=True, text=True)

print(gittag.stderr)
print(gitpushtag.stderr)