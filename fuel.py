text = input("Fraction:")
x= text.split("/")
#print(x)
if x[0].isdigit() and x[1].isdigit():
    if x[1] != "0":
        #print(x[1])
        calc=int(x[0])/int(x[1])
        calc = int(round(calc*100))
        if calc<1 : print("R")
        elif calc > 99: print("F")
        else: print(calc, "%")
#else :
#    print( "not digits")
