HW_SOURCE_FILE = 'hw04.py'

###############
#  Questions  #
###############

def intersection(st, ave):
    """Represent an intersection using the Cantor pairing function."""
    return (st+ave)*(st+ave+1)//2 + ave

def street(inter):
    return w(inter) - avenue(inter)

def avenue(inter):
    return inter - (w(inter) ** 2 + w(inter)) // 2

w = lambda z: int(((8*z+1)**0.5-1)/2)

def taxicab(a, b):
    """Return the taxicab distance between two intersections.

    >>> times_square = intersection(46, 7)
    >>> ess_a_bagel = intersection(51, 3)
    >>> taxicab(times_square, ess_a_bagel)
    9
    >>> taxicab(ess_a_bagel, times_square)
    9
    """
    "*** YOUR CODE HERE ***"
    return abs(street(a)-street(b))+abs(avenue(a)-avenue(b))

def squares(s):
    """Returns a new list containing square roots of the elements of the
    original list that are perfect squares.

    >>> seq = [8, 49, 8, 9, 2, 1, 100, 102]
    >>> squares(seq)
    [7, 3, 1, 10]
    >>> seq = [500, 30]
    >>> squares(seq)
    []
    """
    "*** YOUR CODE HERE ***"
    lst=[]
    for n in s:
        root = n**0.5
        if root.is_integer() and int(root) not in lst:
            lst.append(int(root))
    return lst

def g(n):
    """Return the value of G(n), computed recursively.

    >>> g(1)
    1
    >>> g(2)
    2
    >>> g(3)
    3
    >>> g(4)
    10
    >>> g(5)
    22
    >>> from construct_check import check
    >>> check(HW_SOURCE_FILE, 'g', ['While', 'For'])
    True
    """
    "*** YOUR CODE HERE ***"
    assert n > 0
    if n <= 3:
        return n
    else:
        return g(n-1)+2*g(n-2)+3*g(n-3)

def g_iter(n):
    """Return the value of G(n), computed iteratively.

    >>> g_iter(1)
    1
    >>> g_iter(2)
    2
    >>> g_iter(3)
    3
    >>> g_iter(4)
    10
    >>> g_iter(5)
    22
    >>> from construct_check import check
    >>> check(HW_SOURCE_FILE, 'g_iter', ['Recursion'])
    True
    """
    "*** YOUR CODE HERE ***"
    assert n > 0
    if n <= 3:
        return n
    else:
        a, b, c = 3, 2, 1
        i = 0
        while i < n-3:
            a, b, c = a+b*2+c*3, a, b
            i += 1
    return a


def pingpong(n):
    """Return the nth element of the ping-pong sequence.

    >>> pingpong(7)
    7
    >>> pingpong(8)
    6
    >>> pingpong(15)
    1
    >>> pingpong(21)
    -1
    >>> pingpong(22)
    0
    >>> pingpong(30)
    6
    >>> pingpong(68)
    2
    >>> pingpong(69)
    1
    >>> pingpong(70)
    0
    >>> pingpong(71)
    1
    >>> pingpong(72)
    0
    >>> pingpong(100)
    2
    >>> from construct_check import check
    >>> check(HW_SOURCE_FILE, 'pingpong', ['Assign', 'AugAssign'])
    True
    """
    "*** YOUR CODE HERE ***"
    def helper(i,sign,last_result):
        if i == n:
            return last_result+sign
        else:
            if has_seven(i) or i%7 == 0:
                return helper(i+1, -sign, last_result+sign)
            else:
                return helper(i+1, sign, last_result+sign)

    return helper(1,1,0)
    # A1
    # i, s = 1, 0
    # key = 1
    # while i<=n:
    #     s = s+key
    #     if has_seven(i) or i%7 == 0:
    #         key = -key
    #     i = i+1
    # return s

    #A3
    # def record_change(i):
    #     if i <= 1:
    #         return 0,0,1
    #     else:
    #         last_id, last_sum, sign = record_change(i-1)
    #         if has_seven(i) or (i)%7 == 0:
    #             return i, last_sum+(i-last_id)*sign,-sign
    #         else:
    #             return last_id, last_sum, sign
    # lastid, lastsum, sign = record_change(n)
    # return lastsum+(n-lastid)*sign
    
    # A2
    # def sign(i):
    #     if i <= 1:
    #         return 1
    #     else:
    #         if has_seven(i) or i%7 == 0:
    #             return -sign(i-1)
    #         else:
    #             return sign(i-1)

    # if n <= 2:
    #     return n
    # else:
    #     return pingpong(n-1)+sign(n)

def has_seven(k):
    """Returns True if at least one of the digits of k is a 7, False otherwise.

    >>> has_seven(3)
    False
    >>> has_seven(7)
    True
    >>> has_seven(2734)
    True
    >>> has_seven(2634)
    False
    >>> has_seven(734)
    True
    >>> has_seven(7777)
    True
    """
    if k % 10 == 7:
        return True
    elif k < 10:
        return False
    else:
        return has_seven(k // 10)

def count_change(amount):
    """Return the number of ways to make change for amount.

    >>> count_change(7)
    6
    >>> count_change(10)
    14
    >>> count_change(20)
    60
    >>> count_change(100)
    9828
    """
    "*** YOUR CODE HERE ***"
    def max(n):
        i=0
        while 2**i <= n:
            i +=1
        return i-1  #count of types of coins

    def count_partitions(n, m):
        """Count the ways to partition n using parts up to m."""
        if n < 0:
            return 0
        if n == 0:
            return 1
        elif m < 1 :
            return 0
        elif m == 1:
            return 1
        else:
            s=0
            for i in range(0,n//m+1):
                s +=  count_partitions(n-m*i, int(m/2))
            return s

    return count_partitions(amount,2**max(amount))






###################
# Extra Questions #
###################

from operator import sub, mul

def make_anonymous_factorial():
    """Return the value of an expression that computes factorial.

    >>> make_anonymous_factorial()(5)
    120
    >>> from construct_check import check
    >>> check(HW_SOURCE_FILE, 'make_anonymous_factorial', ['Assign', 'AugAssign', 'FunctionDef', 'Recursion'])
    True
    """
    pass
