import re
import sys


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    matches= re.search(r"^(.+)\.(.+)\.(.+)\.(.+)$", ip)
    if(matches):
        if ((int(matches.group(1)) <= 255 ) and
        (int(matches.group(2)) <= 255 ) and
        (int(matches.group(3)) <= 255 ) and
        (int(matches.group(4)) <= 255 )):
            return True
        else:
            return False
    else:
        return False

    #print(ip)
    #print(matches.group(1))





if __name__ == "__main__":
    main()
