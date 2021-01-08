read_file ='read.txt'
write_file ='write.txt'
translate = {
    'one': 'один',
    'two': 'два',
    'three': 'три',
    'four': 'четыри',
}
with open(read_file, 'r', encoding='UTF-8') as f:
    lines = f.readlines()
    new_lines = [f'{translate[line.split("-")[0]]} - {line.split("-")[-1]}' for line in lines]
with open(write_file, 'w', encoding='UTF-8') as f:
    f.writelines(new_lines)