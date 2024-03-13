def save(t, path="todo.txt"):
    """
    It saves the todo list on the local file todo.txt
    :param path: file path
    :param t: todo list
    :return: None
    """
    with open(path, "w") as f:
        f.writelines(t)
        print(t)


def get_todos(path="todo.txt"):
    """
    It gets the todo list from the file todo.txt
    :param path: file path
    :return: todo list
    """
    with open(path, "r") as f:
        t = f.readlines()
    return t
