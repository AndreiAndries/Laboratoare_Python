import auxiliar_functions


# Write a function to return a list of the first n numbers in the Fibonacci string.
def fibonacci(n):
    if n == 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        a = [0, 1]
        while len(a) < n:
            a.append(a[-1] + a[-2])
        return a


# Write a function that receives a list of numbers and returns a list of the prime numbers found in it.
def prime_numbers(li):
    a = []
    for i in li:
        if auxiliar_functions.prime(i):
            a.append(i)
    return a


# Write a function that receives as parameters two lists a and b and returns: (a intersected with b, a reunited with
# b, a - b, b - a)
def operations(a, b):
    e = [auxiliar_functions.lists_reunited(a, b), auxiliar_functions.lists_intersected(a, b),
         auxiliar_functions.minus(a, b), auxiliar_functions.minus(b, a)]
    return e


# Write a function that receives as a parameters a list of musical notes (strings), a list of moves (integers) and a
# start position (integer). The function will return the song composed by going though the musical notes beginning
# with the start position and following the moves given as parameter.
def musical_notes(notes, moves, start):
    if start < 0:
        start *= -1
    if start > len(notes):
        start = start % len(notes)
    e = [notes[start]]
    for i in moves:
        start += i
        if start < 0:
            start *= -1
        if start > len(notes):
            start = start % len(notes)
        e.append(notes[start])
    return e


# Write a function that receives as parameter a matrix and will return the matrix obtained by replacing all the
# elements under the main diagonal with 0 (zero).
def matrix_diagonal(matrix):
    for i in range(0, len(matrix)):
        matrix[i][i] = 0
    for i in matrix:
        print(i)


# Write a function that receives as a parameter a variable number of lists and a whole number x. Return a list
# containing the items that appear exactly x times in the incoming lists.
def number_of_x_elements(lists, x):
    s = lists.copy()
    counter = []
    for i in s:
        for c in i:
            if not counter:
                counter.append([c, 1])
            else:
                app = False
                for clone in counter:
                    if clone[0] == c:
                        clone[1] += 1
                        app = True
                if not app:
                    counter.append([c, 1])
    e = []
    for i in counter:
        if i[1] == x:
            e.append(i[0])
    print(e)


# Write a function that receives as parameter a list of numbers (integers) and will return a tuple with 2 elements.
# The first element of the tuple will be the number of palindrome numbers found in the list and the second element
# will be the greatest palindrome number.
def palindrome_numbers(myList):
    counter = 0
    maxim = 0
    for i in myList:
        if auxiliar_functions.palindrome(i):
            if maxim < i:
                maxim = i
            counter += 1
    e = (counter, maxim)
    return e


# Write a function that receives a number x, default value equal to 1, a list of strings, and a boolean flag set to
# True. For each string, generate a list containing the characters that have the ASCII code divisible by x if the
# flag is set to True, otherwise it should contain characters that have the ASCII code not divisible by x.
def ascii_codes(my_list, x=1, flag=True):
    return_list = []
    for i in my_list:
        e = []
        chars = [*i]
        for c in chars:
            if flag:
                if not int(ord(c)) % x:
                    e.append(c)
            else:
                if int(ord(c)) % x:
                    e.append(c)
        return_list.append(e)
    return return_list


# Write a function that receives as paramer a matrix which represents the heights of the spectators in a stadium and
# will return a list of tuples (line, column) each one representing a seat of a spectator which can't see the game. A
# spectator can't see the game if there is at least one taller spectator standing in front of him. All the seats are
# occupied. All the seats are at the same level. Row and column indexing starts from 0, beginning with the closest
# row from the field.
def tall_spectators(matrix):
    e = []
    for i in range(0, len(matrix) - 1):
        for j in range(0, len(matrix) - 1):
            if matrix[i][j] < matrix[i + 1][j]:
                e.append((i, j))
    return e


# Write a function that receives a variable number of lists and returns a list of tuples as follows: the first tuple
# contains the first items in the lists, the second element contains the items on the position 2 in the lists, etc.
def right_rotation(matrix):
    e = []
    for i in matrix:
        while len(i) < len(matrix):
            i.append("")
    for i in range(0, len(matrix)):
        a = []
        for j in range(0, len(matrix)):
            a.append(matrix[j][i])
        e.append(tuple(a))
    print()
    for i in e:
        print(i)
    print()


if __name__ == '__main__':
    print(fibonacci(12))
    print(prime_numbers([1, 2, 5, 4, 7, 23, 665, 21, 45, 90, 11, 88, 7, 5]))
    print(operations([1, 5, 8, 4, 2], [2, 5, 8, 5, 6]))
    print(musical_notes(["do", "re", "mi", "fa", "sol"], [1, -3, 4, 2], 2))
    print()
    matrix_diagonal([[2, 3, 5, 7], [3, 5, 7, 9], [3, 5, 76, 7], [6, 4, 32, 1]])
    print()
    number_of_x_elements([[1, 2, 3], [2, 3, 4], [4, 5, 6], [4, 1, "test"]], 2)
    print(palindrome_numbers([121, 4, 33, 112, 5467, 354, 1111, 789, 777]))
    print(ascii_codes(x=2, my_list=["test", "hello", "lab002"], flag=False))
    print(tall_spectators([[1, 2, 3, 2, 1, 1], [2, 4, 4, 3, 7, 2], [5, 5, 2, 5, 6, 4], [6, 6, 7, 6, 7, 5]]))
    right_rotation([[1, 2, 3], [5, 6, 7], ["a", "b", "c"]])
