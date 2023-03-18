def join(*args, sep='-'):
    """
    :param args: collection of lists
    :param sep: a seperator between the lists
    :return: concatenation of all list with seperator between them
    """
    if not args:
        return None
    joined_lists = []
    for arg in args:
        # The task did not specify what to do in case it's not a list.
        if not isinstance(arg, list):
            print("Can only accept lists")
            return None
        joined_lists += arg + [sep]
    return joined_lists[:-1]

