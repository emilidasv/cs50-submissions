import validators

def main():
    text = input("What's your email address?")
    if(validate_email(text)):
        print("Valid")
    else:
        print("Invalid")

def validate_email(text):
    if(validators.email(text)): return True
    else: return False


if __name__ == "__main__":
    main()
