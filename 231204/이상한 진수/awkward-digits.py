a = input()
b = input()

def find_case2(string):
    if string[0] == '0':
        return [int(string[1:], 2)]

    _list = []

    for i in range(len(string)):
        if string[i] == "1" and i != 0:
            temp = list(string)
            temp[i] = "0"
            _list.append(int(''.join(temp), 2))

        if string[i] == "0":
            temp = list(string)
            temp[i] = "1"
            _list.append(int(''.join(temp), 2))

    return _list
        
def find_case3(string):
    if string[0] == '0':
        return [int(string[1:], 3)]

    _list = []

    for i in range(len(string)):
        if i == 0:
            if string[i] == "1":
                temp = list(string)
                temp[i] = "2"
                _list.append(int(''.join(temp), 3))
            if string[i] == "2":
                temp = list(string)
                temp[i] = "1"
                _list.append(int(''.join(temp), 3))


        else:
            for n in range(3):
                if int(string[i]) != n:
                    temp = list(string)
                    temp[i] = str(n)
                    _list.append(int(''.join(temp), 3))



        return _list


la = find_case2(a)
lb = find_case3(b)

n = set(la) & set(lb)

print(*n)