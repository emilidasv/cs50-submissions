    i = 1
        output_string = "Adieu, Audie,"
        print("amount_of_arg", amount_of_arg)
        while i < amount_of_arg :
            if amount_of_arg == 2:
                output_string =output_string + " to " +  sys.argv[1]
                print(output_string)
                i=i+1
            elif amount_of_org == 3:
                print("hej", i)
                output_string ==output_string + "  and " +  sys.argv[i]
