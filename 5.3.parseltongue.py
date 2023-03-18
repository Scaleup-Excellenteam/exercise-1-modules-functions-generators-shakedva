import re

MSG_PATTERN = r"([a-z]{5,}!)"
CHUNK_SIZE = 1024


def find_hidden_messages(path):
    with open(path, "rb") as file:
        while True:
            chunk = file.read(CHUNK_SIZE)
            if not chunk:
                break
            yield re.findall(MSG_PATTERN, str(chunk))


for hidden_messages in find_hidden_messages("logo.jpg"):
    for msg in hidden_messages:
        print(msg)
