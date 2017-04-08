# Input - findvowels.py animals
# Assignment Part 1
# Output - The word animals have 3 vowels
# Assignment Part 2
# Output - The word animals have 3 vowels, 2 a, 1 i

import sys
word1 = sys.argv[1]
word2 = sys.argv[2]
#print (sys.argv[1] + " " + sys.argv[2])



def findvowels(word):

    word_split = list(word)
    count = 0

    for letter in word_split:
        print(letter)
        if letter == 'a' or letter == 'i' or letter == 'e' or letter == 'o' or letter == 'u':
            print ("this letter is a vowel")
            count = count + 1
        else:
            print('this letter is not a vowel')

    print(word)

    print("the total number of vowels in " + str(word) + " is " + str(count))
    return;

findvowels(word2)


