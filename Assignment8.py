import os

# Get the folder where this Python file is located
folder = os.path.dirname(os.path.abspath(__file__))

input_file = os.path.join(folder, "input.txt")
output_file = os.path.join(folder, "output.txt")

# Read data from input file
with open(input_file, "r") as file:
    lines = file.readlines()

# Count total lines
print("Total number of lines:", len(lines))

# Extract first two lines
first_two_lines = lines[:2]

print("\nFirst two lines:")
for line in first_two_lines:
    print(line.strip())

# Write first two lines into output file
with open(output_file, "w") as file:
    file.writelines(first_two_lines)

print("\nFirst two lines written successfully to output.txt")

input.txt
Hello, this is the first line.
This is the second line.
This is the third line.
This is the fourth line.
This is the fifth line.
Comment:-
  Total number of lines: 5

First two lines:
Hello, this is the first line.
This is the second line.

First two lines written successfully to output.txt
