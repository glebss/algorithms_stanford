import time

def read_arr(arr_path):
    with open(arr_path, 'r') as f:
        data = f.readlines()
        data = [int(d.strip()) for d in data[1:]]
        data = [(str(i+1), data[i]) for i in range(len(data))]
    return data

if __name__ == '__main__':
    tic = time.time()
    arr_path = "../data/huffman.txt"
    data = read_arr(arr_path)
    data = sorted(data, key=lambda x: x[-1], reverse=True)
    codes = {d[0]: '' for d in data}
    while len(data) > 1:
        first_el = data.pop()
        second_el = data.pop()
        first_char, second_char = first_el[0], second_el[0]
        for char in first_char.split('_'):
            codes[char] = '1' + codes[char]
        for char in second_char.split('_'):
            codes[char] = '0' + codes[char]

        new_char = first_char + '_' + second_char
        new_freq = first_el[-1] + second_el[-1]
        if not data:
            break
        # find a place where to insert new element
        for i in range(len(data)-1, -1, -1):
            if data[i][-1] > new_freq:
                break
        if i == len(data)-1:
            data.append((new_char, new_freq))
        elif i == 0:
            if data[0][-1] > new_freq:
                data.insert(1, (new_char, new_freq))
            else:
                data.insert(0, (new_char, new_freq))
        else:
            data.insert(i+1, (new_char, new_freq))
    print(min([len(v) for v in codes.values()]), max([len(v) for v in codes.values()]))
    toc = time.time()
    print(toc-tic)
