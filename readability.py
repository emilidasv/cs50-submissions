# TODO
from cs50 import get_string
import re


def main():
    userInputtext = get_string("please give me the text:")
    lenoftext1 = len(userInputtext)


    # Splitting a string with .split()
    words = userInputtext.split()
    ## debug print("Words", words)

    ## count number of words in the string
    numberofwords = len(words)
    ## debug print("number of words", numberofwords)

    # first count the number of letters in each word
    letters = [len(item) for item in words]

    # count the total number of words
    numbersofletters = 0
    for elem in range(len(letters)):
        numbersofletters = numbersofletters + letters[elem]
    ## debug print("letters", numbersofletters)

    # calculate numbers of sentences
    sentences = re.split(r'[.!?]+', userInputtext)
    numberofsentences = len(sentences);
    # import re
    ##debug print("Words", sentences)
    avgletters = 0.0
    avgletters = numbersofletters * 100
    avgletters = avgletters / numberofwords
    avgsentences = (numberofsentences * 100.0) / numberofwords

    readingindex = (0.0588 * avgletters) - (0.296 * avgsentences) - 15.8
    grade = int(round(readingindex))
    if (grade > 16):
        print("Grade 16+")
    elif (grade < 1):
        print("Before Grade 1")
    else :
        print("Grade:", grade)


main()
