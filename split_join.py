def split_and_join(line):
    string_split = line.split()
    char = '-'
    return char.join(string_split)
d = split_and_join('hola soy de america')

print(d)