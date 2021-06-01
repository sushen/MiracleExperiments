line_index = 3
lines = None
with open('file.txt', 'r') as file_handler:
    lines = file_handler.readlines()

lines.insert(line_index, 'Charlie')

with open('file.txt', 'w') as file_handler:
    file_handler.writelines(lines)