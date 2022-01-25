from part2 import run
with open("expect") as infile:
    txt = {tuple(line.strip().split(',')) for line in infile.readlines()}

all_paths = run("test_input1")
diff = set(txt) - set(all_paths)
print("DIFFERENCE:")
for path in diff:
    print(path)

