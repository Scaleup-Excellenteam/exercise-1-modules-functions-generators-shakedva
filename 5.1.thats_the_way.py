from os import listdir

REQUEST = "Enter the folder's path: "
PREFIX = "deep"


def get_files_starting_with(path, prefix):
    """
    :param path: str path to a file
    :param prefix: str
    :return: a list of all the files that starts with the prefix
    """
    return [file for file in listdir(path) if file.startswith(prefix)]


def main():
    """
    Receives a path to a file and prints the number of files inside it with a prefix
    """
    path = input(REQUEST)
    print(len(get_files_starting_with(path, PREFIX)))


if __name__ == "__main__":
    main()
