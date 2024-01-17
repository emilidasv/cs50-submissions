from pyfiglet import Figlet
import sys

figlet = Figlet()

def main():
    figlet_font_dict =[]

    if len(sys.argv) == 0 :
        print("0")
        # Random font
    elif len(sys.argv) == 3 :
        # check first argument
        if (sys.argv[1] != "-f" or sys.argv[1] != "--font" )and not(sys.argv[2] in figlet_font_dict):
            sys.exit("wrong type of arguments")
    else:
        sys.exit("Wrong number of arguments")

    if (len(sys.argv) > 3 ) or (len(sys.argv) == 1):
        print(">3")
        sys.exit("Wrong number of arguments")
    elif len(sys.argv) == 1 ) :
        print("0")
        # Random font
    else:
        # --3
        # check first argument
        if (sys.argv[1] != "-f" or sys.argv[1] != "--font" )and not(sys.argv[2] in figlet_font_dict):
            sys.exit("wrong type of arguments")
        print("==3")







    #figlet.getFonts()

    #figlet.setFont(font=f)
    #print(figlet.renderText(s))




if __name__ == "__main__":
    main()
