import math


def prime(x):
    if x < 2:
        return False
    elif x == 2:
        return True
    else:
        if not x % 2:
            return False
        for i in range(3, int(math.sqrt(x)), 2):
            if not x % i:
                return False
        return True


def remove_duplicates(a):
    e = []
    for i in a:
        if not len(e):
            e.append(i)
        else:
            ok = False
            for j in e:
                if i == j:
                    ok = True
            if not ok:
                e.append(i)
    return e


def lists_reunited(a, b):
    c = a.copy()
    d = b.copy()
    while d:
        c.append(d[0])
        d.pop(0)
    return remove_duplicates(c)


def lists_intersected(a, b):
    c = a.copy()
    d = b.copy()
    e = []
    for i in c:
        for j in d:
            if i == j:
                e.append(i)
    return remove_duplicates(e)


def minus(a, b):
    c = a.copy()
    d = b.copy()
    e = []
    for i in c:
        ok = False
        for j in d:
            if i == j:
                ok = True
        if not ok:
            e.append(i)
    return remove_duplicates(e)

def palindrome(x):
    s = str(x)
    cpy = s
    if s == cpy[::-1]:
        return True
    return False