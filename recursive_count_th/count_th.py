'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    # apathy
    # current == h
    # TBC
    # traverse the string and check if the current character
    # is equal to the word "t" and its next character i + 1 == "h"
    # define a count to keep track of the current character
    # in the string
    i = 0
    count = 0
    length = len(word)
    end = length - 1
    # define a base case
    if length <= 1:
        return 0
    # store current character
    elif i >= end:
        return count
    else:
        current = word[i]
        next = word[i+1]
        # apathy[0] == a
        # check if current character is equal to "t"
        if current == "t" and next == "h":
            count += 1
            return count_th(word)
        else:
            i += 1
            return count_th(word)
    return count
    

new_word = "apathy"
count_th(new_word)
