import os

# List all entries in the current directory
entries = os.listdir('.git/refs/tags')
for entry in entries:
    print(entry)