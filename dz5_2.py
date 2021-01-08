FILE_NAME = 'text.txt'

with open(FILE_NAME, 'r', encoding='UTF-8') as f:
    lines = f.readlines()
    print(f'количество строк в файле: {len(lines)}')
    for i, line in enumerate(lines):
        print(f'количество слов в {i} строке: {len(line.split())}')