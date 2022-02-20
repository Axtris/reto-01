import os

root = R"C:\Users\$USERNAME\Downloads"

dir = os.path.expandvars(root)
print(dir)

listfiles = os.listdir(dir)
print(listfiles)

walk_generator = os.walk(dir)
dir_entry = next(walk_generator)

dir_entry[1] + dir_entry[2]
[os.path.join(dir_entry[0], item) for item in dir_entry[1]+dir_entry[2]]
for entry in walk_generator:
    print(entry)
