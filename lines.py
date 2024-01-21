import sys

def main():

    # loop throug file
    user_arg=sys.argv
    if(check_user_input(user_arg)):
        number_of_rows = 0
        i=0
        with open(user_arg[1], "r") as file:
            for line in file:
                i=i+1
                #print(line)
                #line=line.strip('')
                #print(line)
                #if line[0] != "#" and line[0]!="\n" :
                if(check_line(line)):
                    number_of_rows = number_of_rows + 1
                    #print(i)
                    #print("number_of_rows", number_of_rows)
            print(number_of_rows)

def check_user_input(user_arg):
    # check commanline argument

    if len(user_arg) < 2:
        sys.exit("Too few command-line arguments")
    elif len(user_arg) > 2:
        sys.exit("Too many command-line arguments")
    else:
    # try to open file
        user_input= user_arg[1]
        if ".py" not in sys.argv[1]:
            sys.exit("Not a Python file")
        else:
            if(read_file(user_input)):return True

def read_file(filename):

    try:
        file = open(filename, "r")
        file.close()
        return True
    except:
        #print("File does not exist")
        #raise FileNotFoundError
        sys.exit(FileNotFoundError)

def check_line(line):
    print("line", line)
    if line.isspace():
        print("False ispace")
        return False
    if line.strip().startswith("#"):
        print("False #")
        return False

    else:
        print("True")
        return True



if __name__ == "__main__":
    main()
