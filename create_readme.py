## This script creates the readme files for each direcotry i have
import csv
import os

csv_file = "./titles.csv"

with open(csv_file, mode='r') as file:
    reader = csv.reader(file)
    next(reader)  # Skip header row
    data = list(reader)

directories = [dir for dir in os.listdir(".") if os.path.isdir(dir) and dir.startswith("day")]
days = {row[0]: (row[1], row[2]) for row in data}

# # Iterate through directories
for  directory in directories:
    if directory in days:
        d = days[directory]
        readme_content = f"# {directory}, {d[0]}, {d[1]}"
        readme_file = os.path.join(directory, "readme.md")
        with open(readme_file, mode='w') as readme:
            readme.write(readme_content)
        print(f"README.md created for {directory}")
