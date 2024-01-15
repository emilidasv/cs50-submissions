do_continue = True
while do_continue:
    try:
        text = input("Fraction:")
        x= text.split("/")
        if x[0].isdigit() and x[1].isdigit():
            if x[1] != "0":
                calc=int(x[0])/int(x[1])
                do_continue = False
                calc = int(round(calc*100))
                if calc <= 1 : print("E")
                elif calc >= 99: print("F")
                else:
                    calc_str = str(calc)
                    calc_str = calc_str + "%"
                    print(calc_str)

    except ValueError:
            pass


