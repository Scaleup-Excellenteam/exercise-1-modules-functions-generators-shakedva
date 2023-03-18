from os import listdir


def get_files_starting_with(path, prefix):
    """
    :param path: to a file
    :param prefix:
    :return: a list of all the files that starts with the prefix
    """
    return [file for file in listdir(path) if file.startswith(prefix)]


path = input("Enter the folder's path: ")
print(len(get_files_starting_with(path, 'deep')))
