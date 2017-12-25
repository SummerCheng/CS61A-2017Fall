## Generators

def make_generators_generator(g):
    """Generates all the "sub"-generators of the generator returned by
    the generator function g.
    >>> def ints_to(n):
    ...     for i in range(1, n + 1):
    ...          yield i
    ...
    >>> def ints_to_5():
    ...     for item in ints_to(5):
    ...         yield item
    ...
    >>> for gen in make_generators_generator(ints_to_5):
    ...     print("Next Generator:")
    ...     for item in gen:
    ...         print(item)
    ...
    Next Generator:
    1
    Next Generator:
    1
    2
    Next Generator:
    1
    2
    3
    Next Generator:
    1
    2
    3
    4
    Next Generator:
    1
    2
    3
    4
    5
    """
    "*** YOUR CODE HERE ***"
    # def helper(times):
    #     i=1
    #     while i <= times:
    #         yield i
    #         i+=1

    # gen = g()
    # while True:
    #     yield helper(next(gen))

    def helper(times):
        i=1
        gen = g()
        while i <= times:
            yield next(gen)
            i += 1

    i = 1
    while i <= len(list(g())):
        yield helper(i)
        i += 1





    # def helper(times):
    #     i = 0

    #         next(g)
    #         i+=1
    # i = 1
    # while helper(i) != g:
    #     yield helper(i)
    #     i += 1




def permutations(lst):
    """Generates all permutations of sequence LST. Each permutation is a
    list of the elements in LST in a different order.

    The order of the permutations does not matter.

    >>> sorted(permutations([1, 2, 3]))
    [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]
    >>> type(permutations([1, 2, 3]))
    <class 'generator'>
    >>> sorted(permutations((10, 20, 30)))
    [[10, 20, 30], [10, 30, 20], [20, 10, 30], [20, 30, 10], [30, 10, 20], [30, 20, 10]]
    >>> sorted(permutations("ab"))
    [['a', 'b'], ['b', 'a']]
    """
    if not lst:
        yield []
        return
    "*** YOUR CODE HERE ***"
    length=len(lst)
    if length == 1:
        yield lst
        return
    else:
        for i in range(length):
            lst1=list(lst)
            for j in permutations(lst1[0:i]+lst1[i+1:length]):
                yield [lst1[i]]+j
            # j =0
            # while j < len(list(tail)):
            #     yield [lst[i]]+ next(tail)
            #     j += 1

