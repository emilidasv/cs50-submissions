import sys


def main():
    # make sure user input is as expected, number and type
    #exactly one commane line argument
    user_arg=sys.argv
    #print(user_arg)
    if(read_arg(user_arg)):
        file_name=user_arg[1]
        # if all OK open the file and check that file actually is an py fle
        print(file_name)
        if (read_file(file_name)) == FileNotFoundError:
            print("ja")
        else:
            print("nej")
            number_of_rows=calculate_numbers_of_rows(file_name)
            print(number_of_rows)



def read_arg(user_arg):

    if len(user_arg) < 2:
        print("Too few command-line arguments")
        return False
    elif len(user_arg) > 2:
        print("Too many command-line arguments")
        return False
    else:
        user_input= user_arg[1]
        try:
            input, py = user_input.split('.py')
        except:
            print("Not a Python file")
            return False
        if input and not(py) :

            return True
        else:
            print("Not a Python file")
            return False

def read_file(filename):

    try:
        file = open(filename, "r")
        file.close()
        return True
    except:
        #print("File does not exist")
        #raise FileNotFoundError
        sys.exit()

def calculate_numbers_of_rows(filename):
     number_of_rows = 0
     i=0
     with open(filename, "r") as file:
        for line in file:
            if (line[0] != "#" and line[0] !="\n"):
                number_of_rows = number_of_rows + 1
        #print("number_of_rows", number_of_rows)
        return number_of_rows


if __name__ == "__main__":
    main()
