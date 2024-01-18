import sys
import inflect



def main():
    p = inflect.engine()
    output=""
    while (True):
        try:
            item = input("")
            output= output + item +","
        except EOFError:
            break

    #strip the last coma
    output = output[0:len(output)-1]
    output2 = output.split(",")
    #print(mylist)
    #print(output2)
    #print(len(output2))

    if (len(sys.argv) == 1 ):
        output_string = "Adieu, Audie, to " + p.join((output2))
    else:
        sys.exit("Wrong number of arguments")

    #print("")
    print(output_string )

if __name__ == "__main__":
    main()
