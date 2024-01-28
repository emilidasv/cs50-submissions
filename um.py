import re
import sys


def main():
    print(count(input("Text: ")))


def count(s):
    s = s.split(" ")
    print(s)
    count_um = 0
    for word in s:
        print(word)
        if matches := re.search(r'^um\b(\,|\?|\.)?$', word ,re.IGNORECASE):
            count_um = count_um + 1
    #print(count_um)
    return count_um






...


if __name__ == "__main__":
    main()
