# file = open("reading.txt")

# print(file)

# lines = file.readlines()

# file.close()

with open("reading.txt") as file:
    lines = file.readlines()

print(lines)

for line in lines:
    print(line.strip())