input_str = input()
obj_str = input()

def find():
    input_idx = 0
    obj_idx = 0
    start = 0

    while(input_idx < len(input_str)):
        if(input_str[input_idx] == obj_str[obj_idx]):
            input_idx += 1
            obj_idx += 1
            
            if obj_idx == len(obj_str):
                return input_idx - obj_idx

        else:
            input_idx += 1
            obj_idx = 0

    return -1

print(find())