""" Palindrome """
# Created by Yenami
# Date : May 21, 2017


def is_palindrome(word):

    # devide word in 2
    middle1 = middle2 = []
    long_word = len(word)
    long_middle_word = int(long_word/2)

    # first middle
    for i in range(0,long_middle_word):
        middle1.append(word[i])

    # second middle
    for j in reversed(range(long_word-1,long_middle_word,-1)):
        middle2.append(word[j])

    # first middle = reverse(second middle)
    if middle1 == middle2[::-1] :
        bool = True
        print("The word "+word+" is a palindrome!")
    else:
        bool = False
        print("The word "+word+" is not a palindrome!")
    return bool

# call function with one word
print(is_palindrome('kayak'))
