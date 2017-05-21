""" Palindrome """
# Created by Yenami
# Date : May 21, 2017

# devide word in 2
middle1 = []
middle2 = []

def is_palindrome(word):
    long_middle_word = int(len(word)/2)
    # first middle
    for i in range(0,long_middle_word):
        middle1.append(word[i])
    l = int(len(word))
    # second middle
    for j in reversed(range(l-1,long_middle_word,-1)):
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
