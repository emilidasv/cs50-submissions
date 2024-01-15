text = input("Fraction:")
x= text.split("/")
#print(x)
if x[0].isdigit() and x[1].isdigit():
    if x[1] != "0":
        #print(x[1])
        try:
            calc=int(x[0])/int(x[1])
            calc = int(round(calc*100))
            if calc < 1 : print("E")
            elif calc > 99: print("F")
            else:
                calc_str = str(calc)
                calc_str = calc_str + "%"
                print(calc_str)
        except ValueError:
            c=1

#else :
#    print( "not digits")

