def main():
    text = input("Input:")
    print("Output:" ,convert_to_twittr(text))

def convert_to_twittr(text):
    newtext=""
    for c in text:
        if  (c.upper() in ["A", "E", "I", "O", "U"]):
            newtext = newtext
        else:
            newtext = newtext+c
    return newtext


if __name__ == "__main__":
    main()
