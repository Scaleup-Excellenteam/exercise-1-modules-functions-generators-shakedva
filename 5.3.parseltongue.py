import re

# regex for all words in english lower-case letters, that contain at least 5 characters and end with exclamation mark
MSG_PATTERN = r"([a-z]{5,}!)"
CHUNK_SIZE = 1024

FILE_PATH = "C:\Users\shake\Desktop\College\4th Year\Semester B\Excellenteam\python\Ex\exercise-1-modules-functions-generators\logo.jpg"


def find_hidden_messages(path):
    """
    a generator that receives a path to a binary file and yields hidden messages that fit MSG_PATTERN from it.
    :param path: to a binary file
    :return:
    """
    start = 0  # represent where we start reading from the file
    with open(path, "rb") as file:
        chunk = file.read(CHUNK_SIZE)
        while chunk:
            yield re.findall(MSG_PATTERN, str(chunk))
            start += CHUNK_SIZE
            file.seek(start)
            chunk = file.read(CHUNK_SIZE)


def main():
    """
    Calls find_hidden_messages function to find hidden messages in an image
    """
    for hidden_messages in find_hidden_messages(FILE_PATH):
        for msg in hidden_messages:
            print(msg)


if __name__ == "__main__":
    main()
