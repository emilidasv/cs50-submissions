import sys
import inflect



def main():
    if (len(sys.argv) != 1 ):
        sys.exit("Wrong number of arguments")
    else:


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
        output_string = "Adieu, adieu, to " + p.join((output2))


        print(output_string )

if __name__ == "__main__":
    main()
