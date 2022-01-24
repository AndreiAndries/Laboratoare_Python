# Find The greatest common divisor of multiple numbers read from the console.
def cmmdc(x, y):
    if x == 0:
        return y
    if y == 0:
        return x
    while x != y:
        if x > y:
            x -= y
        else:
            y -= x
    return x


# Write a script that calculates how many vowels are in a string
def number_of_vowles(s):
    a = s.lower()
    return a.count("a") + a.count("e") + a.count("i") + a.count("o") + a.count("u")


# Write a script that receives two strings and prints the number of occurrences of the first string in the second.
def number_of_occurrences(s, s1):
    return s.count(s1)


# Write a script that converts a string of characters written in UpperCamelCase into lowercase_with_underscores.
def lowercase_with_underscores(s):
    a = ""
    first = True
    for c in s:
        if c.isupper() and not first:
            a = a + "_" + c.lower()
        elif c.isupper() and first:
            a = a + c.lower()
            first = False
        else:
            a += c

    return a


# Given a square matrix of characters write a script that prints the string obtained by going through the matrix in
# spiral order (as in the example):
def translate_matrix_in_spiral(matrix):
    a = ""
    while matrix:
        array = matrix[0]
        for c in array:
            a += c
        matrix.pop(0)
        for c in matrix:
            a += c[-1]
            c.pop(len(c) - 1)
        array = matrix[-1]
        cpy = ""
        for c in array:
            cpy += c
        a += cpy[::-1]
        matrix.pop(len(matrix) - 1)
        cpy = ""
        for c in matrix:
            cpy += c[0]
            c.pop(0)
        a += cpy[::-1]
    return a


# Write a function that validates if a number is a palindrome.
def palindrom(x):
    s = str(x)
    cpy = s
    if s == cpy[::-1]:
        return "Este Palindrom"
    return "Nu este Palindrom"


# Write a function that extract a number from a text (for example if the text is "An apple is 123 USD", this function
# will return 123, or if the text is "abc123abc" the function will extract 123). The function will extract only the
# first number that is found.
def extract_first_number(x):
    s = x.replace(" ", "")
    if s.isalnum():
        a = ""
        gata = False
        start = False
        for c in s:
            if gata:
                break
            else:
                if c.isdigit():
                    if not start:
                        start = True
                    a += c
                else:
                    if start:
                        gata = True
        if a == "":
            a = "Nu sunt numere"
        return a


# Write a function that counts how many bits with value 1 a number has. For example for number 24,
# the binary format is 00011000, meaning 2 bits with value "1"
def cout_bits(number):
    s = 0
    while number > 0:
        c = number % 2
        s += c
        number = number // 2
    return s


# Write a functions that determine the most common letter in a string. For example if the string is "an apple is not
# a tomato", then the most common character is "a" (4 times). Only letters (A-Z or a-z) are to be considered. Casing
# should not be considered "A" and "a" represent the same character.
def most_common_letter(string):
    s = string.replace(" ", "")
    counter = []
    for c in s:
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
    maxNumber = 0
    letter = ""
    for clone in counter:
        if clone[1] > maxNumber:
            maxNumber = clone[1]
            letter = clone[0]
    return [letter, maxNumber]


# Write a function that counts how many words exists in a text. A text is considered to be form out of words that
# are separated by only ONE space. For example: "I have Python exam" has 4 words.
def number_of_words(string):
    counter = 1
    for c in string:
        if c.isspace():
            counter += 1
    return counter


if __name__ == '__main__':
    print("First number:", end=' ')
    nr1 = int(input())
    print("Second number:", end=' ')
    nr2 = int(input())
    print(cmmdc(nr1, nr2), number_of_vowles("Andrei"), number_of_occurrences("andreiandreiandreiandrei", "andrei"))
    print(lowercase_with_underscores("AnaAreMere"))
    print(translate_matrix_in_spiral
          ([["f", "i", "r", "s"], ["n", "_", "l", "t"], ["o", "b", "a", "_"], ["h", "t", "y", "p"]]))
    print(palindrom(121))
    print(palindrom(122))
    print(extract_first_number("An apple is 123 USD"))
    print(extract_first_number("An apple is some USD"))
    print(extract_first_number("abc123abc"))
    print(cout_bits(24))
    print(most_common_letter("an apple is not a tomato"))
    print("\"I have Python exam\" has", number_of_words("I have Python exam"), "words")
