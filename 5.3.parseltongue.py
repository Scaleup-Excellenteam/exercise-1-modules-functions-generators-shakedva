import re

# regex for all words in english lower-case letters, that contain at least 5 characters and end with exclamation mark
MSG_PATTERN = r"([a-z]{5,}!)"
CHUNK_SIZE = 1024


def find_hidden_messages(path):
    """
    a generator that receives a path to a binary file and yields hidden messages that fit MSG_PATTERN from it.
    :param path: to a binary file
    :return:
    """
    with open(path, "rb") as file:
        while True:
            chunk = file.read(CHUNK_SIZE)
            if not chunk:
                break
            yield re.findall(MSG_PATTERN, str(chunk))


for hidden_messages in find_hidden_messages("logo.jpg"):
    for msg in hidden_messages:
        print(msg)
