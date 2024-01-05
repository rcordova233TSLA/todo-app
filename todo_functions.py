from datetime import datetime
WRITE_TIME = datetime.now()
FILE_NAME = f'todo_{WRITE_TIME.month}-{WRITE_TIME.day}-{WRITE_TIME.year}.txt'


def get_todos(file_path= FILE_NAME)-> list:
    """Get all items currently in to do list"""
    try:
        with open(file_path, 'r') as fh_local:
            todos = [x.strip() for x in fh_local.readlines()]
    except FileNotFoundError:
        return []
    return todos


def write_todos(todos:list,file_path= FILE_NAME):
    """Write all items from a list to a file path"""
    with open(file_path, 'w') as fh_local:
        fh_local.writelines([f'{x}\n' for x in todos])