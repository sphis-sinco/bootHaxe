import subprocess, datetime, os
from datetime import date
from datetime import datetime

now = datetime.now().time()
today = date.today()

#4mat
version = f"{today.year}{today.month}{today.day}.{now.hour % 12}{"%d" % now.minute}"
print(version)

# git push
# git tag _
# git push origin --tags

def gitstuff():
    gitpush = subprocess.run(["git", "push"], capture_output=True, text=True)
    print('push stats: ' + gitpush.stderr)

    if not (gitpush.stderr == "Everything up-to-date"):
        gittag = subprocess.run(["git", "tag", version], capture_output=True, text=True)
        gitpushtag = subprocess.run(["git", "push", "origin", "--tags"], capture_output=True, text=True)

        print('make tag: ' + gittag.stderr)
        print('push tag: ' + gitpushtag.stderr)
    else:
        print("nothing changed dumbo")

foundcurver = False

# List all entries in the current directory
print("tags:")
entries = os.listdir('.git/refs/tags')
for entry in entries:
    if (entry == version):
        foundcurver = True
    print(f" * {entry}")

if (entries.__len__() < 1):
    print(" * none")

if not foundcurver:
    gitstuff()