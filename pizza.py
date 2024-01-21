import sys
import csv
from tabulate import tabulate

def main():
    if(read_arg(sys.argv)):
        file_name=sys.argv[1]
        #print(file_name)
        read_file(file_name)


def read_file(filename):


    #dict_from_csv = dict(list(csv_reader)[0])

    # making a list from the keys of the dict
    #list_of_column_names = list(dict_from_csv.keys())

    with open(filename, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        header_row = reader.fieldnames
        table = []
        #print(table)
        for row in reader:
            #print(row["Regular Pizza"], row["Large"], row["Small"])
            tworows= [row[header_row[0]], row[header_row[1]], row[header_row[2]]]
            table.append(tworows)

    print(tabulate(table, headers = header_row, tablefmt="grid"))



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

