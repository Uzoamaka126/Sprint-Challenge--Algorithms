'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    # define a base case
    if len(word) <= 1:
        return 0
    # store current character
    else:
        if word[0] == "t" and word[1] == "h":
            return 1 + count_th(word[2:])
        else:
            return count_th(word[1:])    

new_word = "apaty"
print(count_th(new_word))
