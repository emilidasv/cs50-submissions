def main():
    text = input("Plate:")
    print(check_if_valid(text))

def check_if_valid(text):
    is_valid = "Valid"
    number_found = False
    if ((len(text) > 6) or len(text) < 2 ): is_valid = "Unvalid"
    if (text[0].isdigit() or text [1].isdigit()) : is_valid = "Unvalid"
    else:
        for c in text:
            if  (c.isdigit()):
                number_found = True
            else:
                if (number_found):is_valid = "Unvalid"
    return is_valid


if __name__ == "__main__":
    main()
