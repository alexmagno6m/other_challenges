def count_substring(string, sub_string):
    count = 0
    if sub_string in string:
        i = 0
        while string.count(sub_string, i, len(string))>0:
            a = string.find(sub_string, i, len(string))
            i = a + 1
            count += 1
        return count
    return count


if __name__ == '__main__':
    string = 'mi perro, es mi perro'
    sub_string = 'es'

    count = count_substring(string, sub_string)
    print(count)