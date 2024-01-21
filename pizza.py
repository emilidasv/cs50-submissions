import sys
import csv
from tabulate import tabulate

def main():
    if(read_arg(sys.argv)):
        file_name=sys.argv[1]
        #print(file_name)
        read_file(file_name)


def read_file(filename):

    with open(filename, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        table = []
        tworows=["Regular Pizza", "Large", "Small"]
        table.append(tworows)
        for row in reader:
            #print(row["Regular Pizza"], row["Large"], row["Small"])
            tworows= [row["Regular Pizza"], row["Large"], row["Small"]]
            table.append(tworows)
    #print(table)
    #table1 = [["Sun",696000,1989100000],["Earth",6371,5973.6],
    #       ["Moon",1737,73.5],["Mars",3390,641.85]]
    #print(tabulate(table, headers = ["Regular Pizza", "Large", "Small"], tablefmt="grid"))
    print(tabulate(table, headers = "firstrow", tablefmt="grid"))



def read_arg(user_arg):
    if len(user_arg) < 2:
        #print("Too few command-line arguments")
        sys.exit("Too few command-line arguments")
    elif len(user_arg) > 2:
        #print("Too many command-line arguments")
        sys.exit("Too many command-line arguments")
    else:
        user_input= user_arg[1]
        try:
            input, py = user_input.split('.csv')
        except:
            #print("Not a Python file")
            sys.exit("Not a CSV file")
        if input and not(py) :

            return True
        else:
            #print("Not a Python file")
            sys.exit("Not a CSV file")

if __name__ == "__main__":
    main()

