import sys

def main():

    # loop throug file
    user_arg=sys.argv
    check_user_input(user_arg)
    number_of_rows = 0
    i=0
    filename=sys.argv[1]
    try:

        with open(filename, "r") as file:
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
    except FileNotFoundError:
            sys.exit("File Not found")



def check_user_input(user_arg):
    # check commanline argument

    if len(user_arg) < 2:
        sys.exit("Too few command-line arguments")
    if len(user_arg) > 2:
        sys.exit("Too many command-line arguments")
    if ".py" not in sys.argv[1]:
        sys.exit("Not a Python file")


def check_line(line):
    if line.isspace():return False
    if line.strip('').startswith("#"):False
    else: return True


if __name__ == "__main__":
    main()
