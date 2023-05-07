def interleave_gen(iterable):
    """
    generator that yields every element from the iterable
    """
    for i in iterable:
        yield i


def interleave(*iterables):
    """
    Combining the elements of the iterables in an alternating pattern, first elements then second elements and so on.
    :param iterables: collection of iterables
    :return: interleave the gives iterables.
    """
    comb_list = []
    sum_len = sum([len(i) for i in iterables])
    # creates a generator for every iterable
    gen_list = [interleave_gen(i) for i in iterables]

    gen_idx = 0
    i = 0
    # extract the current element from the generator
    # if reached the end of the generator (None value) then move to the next generator
    while i < sum_len:
        element = next(gen_list[gen_idx % len(iterables)], None)
        if element is not None:
            comb_list.append(element)
            i += 1
        gen_idx += 1

    return comb_list


def main():
    print(interleave('abc', [1, 2, 3], ('!', '@', '#')))
    print(interleave('abcd', [1, 2, 3]))


if __name__ == "__main__":
    main()
