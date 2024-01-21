import sys
def main():
    ...
    if(check_user_input(sys.argv)):
        print("ja")

def check_user_input(user_arg):
    # check commanline argument

    if len(user_arg) < 3:
        sys.exit("Too few command-line arguments")
    elif len(user_arg) > 3:
        sys.exit("Too many command-line arguments")
    else:
    # try to open file
        user_input= user_arg[1]
        if ".csv" not in sys.argv[1]:
            sys.exit("Not a CSV file")
        else:
            if(search_try_to_open_file(user_input)):
                print("file exits and can ne open")
                return True
        return True

def search_try_to_open_file(filename):

    try:
        file = open(filename, "r")
        file.close()
        return True
    except:
        #print("File does not exist")
        #raise FileNotFoundError
        sys.exit("File not found")

if __name__ == "__main__":
    main()
