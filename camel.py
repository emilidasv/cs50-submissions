def main():
    text = input("Camel case:")
    print("snake case:" ,convert_to_snake(text))

def convert_to_snake(text):
    newtext=""
    for c in text:
        if  (c.isupper()) :
            newtext = newtext +"_" + c[0].lower()
        else:
            newtext = newtext+c
    return newtext


if __name__ == "__main__":
    main()
