def mutate_string(string, position, character):
    str_l = list(string)
    str_l[position] = character
    new_str = ''.join(str_l)
    return new_str

if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)
