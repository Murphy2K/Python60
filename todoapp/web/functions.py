FILEPATH = "todos.txt"


def get_todos(file_path=FILEPATH):
    """ 
    Read todos from a file and return them as a list.
    """
    with open(file_path, "r") as file:
        return file.readlines()

def write_todos(todos, file_path=FILEPATH):
    """
    Write todos to a file.
    """
    with open(file_path, "w") as file:
        file.writelines(todos)
