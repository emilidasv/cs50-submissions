# TODO
from cs50 import get_string
import re


def main():

    userInputtext = get_string("please give me the text:")
#    lenoftext1 = len(userInputtext)
#    print("10 Words", userInputtext)

#    # Splitting a string with .split()
    words = userInputtext.split()
#    print("14 Words", words)

    # count number of words in the string
    numberofwords = len(words)
#    print("18 number of words", numberofwords)

    # first count the number of letters in each word
    letters = [len(item) for item in words]
#    print("22letters", letters)

    # count the total number of words
    numbersofletters = 0
    for elem in range(len(letters)):
        numbersofletters = numbersofletters + letters[elem]
#    print("28 letters", numbersofletters)

    # calculate numbers of sentences

    numberofsentences = userInputtext.count(".") + userInputtext.count("?") + userInputtext.count("!")
#    print("33 numberofsentences", numberofsentences)
    if (numberofsentences != 1) :
        sentences = re.split(r'[.!?]+', userInputtext)

#        print("37 sentences", sentences)
        numberofsentences = len(sentences)
#        print("39 numberofsentences", numberofsentences)

    avgletters = 0.0
    avgletters = numbersofletters * 100.0
    avgletters = avgletters / numberofwords
#    print("44 avgletters", avgletters)

    avgsentences = (numberofsentences * 100.0) / numberofwords
#    print("47 avgsent", avgsentences)

    readingindex = (0.0588 * avgletters) - (0.296 * avgsentences) - 15.8
#    print("50index", readingindex)
#    print("51index", round(readingindex))
#    print("52index", int(round(readingindex)))
#   print("53index", int(readingindex))
#    grade = int(round(readingindex))
    grade = int(readingindex)
    if (grade > 16):
        print("Grade 16+")
    elif (grade < 1):
        print("Before Grade 1")
    else:
        print("Grade:", grade)


main()
