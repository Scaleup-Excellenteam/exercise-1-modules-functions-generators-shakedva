def join(*lists, sep='-'):
    """
    :param lists: collection of lists
    :param sep: a seperator between the lists
    :return: concatenation of all list with seperator between them
    """
    if not lists:
        return None
    lists_with_sep = []
    for lst in lists:
        lists_with_sep = [*lists_with_sep, *lst, sep]
    return lists_with_sep[:-1]


def main():
    """
    Calls the function join with collection of lists and an optional seperator, and prints the result.
    """
    print(join([1, 2], [8], [9, 5, 6], sep='@'))
    print(join([1, 2], [8], [9, 5, 6]))
    print(join([1]))
    print(join())


if __name__ == "__main__":
    main()
