import sys
import csv
def main():
    ...
    if(check_user_input(sys.argv)):
        input_file_argv=sys.argv[1]
        output_file_argv=sys.argv[2]
        print("input", input_file_argv)
        print("output", output_file_argv)
        read_input_file(input_file_argv, output_file_argv)

def read_input_file(input, output):

    with open(input, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        header_row = reader.fieldnames
        table = []
        table.append(header_row)
        #print(table)
        number_of_lines=0
        with open(output, "a") as file:
            writer = csv.DictWriter(file, fieldnames=["Last Name", "First Name", "home"])
            for row in reader:
                #print(row["Regular Pizza"], row["Large"], row["Small"])
                onerow= [row[header_row[0]], row[header_row[1]]]
                lname, fname = onerow[0].split(",")
                home =onerow[1]
                #print(lname, " ", fname, " ", home)
                table.append(onerow)
                number_of_lines = number_of_lines + 1
                writer.writerow({"Last Name": lname, "First Name":fname, "home": home})

            #print(table)
            #print(table[1])
            #print(table[0][1])
            #print(table[1][0].split(","))

        #with open(output) as file:
            #table[0][0] = "Last Name,First name"
            #for line in file:
                #lname, fname =table[i][0].split(",")
                #home = table[i][1]
                #file.append(fname, lname,home)










def check_user_input(user_arg):
    # check commanline argument

    if len(user_arg) < 3:
        sys.exit("Too few command-line arguments")
    elif len(user_arg) > 3:
        sys.exit("Too many command-line arguments")
    else:
    # try to open file
        user_input= user_arg[1]
        if ((".csv" not in sys.argv[1]) or ( ".csv" not in sys.argv[2])):
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
