file_path = "C:/Users/User/Documents/example.txt"


def get_file_info(file_path):
    new_path = ''
    new_name = ''
    new_ext = ''
    for i in range(len(file_path)):
        if file_path[len(file_path) - 1 - i] == ".":
            new_ext += file_path[len(file_path) - 1 - i:]
            break
    for j in range(len(file_path) - len(new_ext)):
        if file_path[(len(file_path) - len(new_ext)) - 1 - j] == '/':
            new_path += file_path[0:((len(file_path) - len(new_ext)) - 1 - j) + 1]
            break
    new_name = file_path[file_path.rfind('/') + 1:file_path.rfind('.')]
    return new_path, new_name, new_ext


print(get_file_info(file_path))
