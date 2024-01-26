import re
import sys


def main():
    print(parse(input("HTML: ")))


def parse(text):
    text = text.strip()
    output=''
    if matches := re.match(r'^(?:<iframe)(?:.*)(?:embed\/)(\w{11})(?:\")(?:.*)', text, re.IGNORECASE):
        output= "https://youtu.be/" + matches.group(1)
    else:
        print("None")
    return output
#<iframe src="http://www.youtube.com/embed/xvFZjo5PgG0"></iframe>

if __name__ == "__main__":
    main()
