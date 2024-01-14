def main():
    text = input("Plate:")
    print(check_if_valid(text))

def check_if_valid(text):
    is_valid = "Valid"
    number_found = False
    if ((len(text) > 6) or len(text) < 2 ): is_valid = "Invalid"
    if (text.isalnum()):
        if (text[0].isdigit() or text [1].isdigit()) : is_valid = "Invalid"
        else:
            for c in text:
                if  (c.isdigit()):
                    number_found = True
                    if c == "0" : is_valid = "Invalid"
                else:
                    if (number_found):is_valid = "Invalid"
    else: is_valid = "Invalid"
    return is_valid


if __name__ == "__main__":
    main()
