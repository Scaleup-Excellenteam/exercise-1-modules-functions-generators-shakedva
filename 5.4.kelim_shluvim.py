def interleave_gen(iterable):
    """
    generator that yields every element from the iterable
    """
    for i in iterable:
        yield i


def interleave(*args):
    """
    :param args: collection of iterables
    :return: list of the iterables' elements
    """
    gen_list = []
    comb_list = []
    sum_len = 0
    # creates a generator for every arg
    for arg in args:
        sum_len += len(arg)
        gen_list.append(interleave_gen(arg))
    i = 0
    gen_idx = 0
    # extract the current element from the generator
    # if reached the end of the generator (None value) then move to the next generator
    while i < sum_len:
        element = next(gen_list[gen_idx % len(args)], None)
        if element is not None:
            comb_list.append(element)
            i += 1
        gen_idx += 1
    return comb_list
