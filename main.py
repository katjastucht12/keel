from itertools import combinations


def sum_not_in_list(numbers_list):
    """
    Returns false if the sum of any two numbers is in the list,
    true otherwise. No type checking, assumes a list of numbers is
    passed in correctly
    :param numbers_list: List of numbers to be processed
    :return: boolean | whether or not the sum is not in the list
    """
    pairs = list(combinations(numbers_list, r=2))
    sums = map(sum, pairs)
    sum_set = set(sums)
    for item in numbers_list:
        if item in sum_set:
            return False
    return True


assert not sum_not_in_list([8, 7, 5, 3])

assert not sum_not_in_list([1, 0])

assert not sum_not_in_list([0, 0])

assert sum_not_in_list([4, 5, 15, 2, 8])

assert sum_not_in_list([])

assert sum_not_in_list([1])

assert sum_not_in_list([5, 5, 5])

assert sum_not_in_list([0])
