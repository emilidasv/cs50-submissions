def main():
    grocery_dict ={}
    #print(grocery_dict)
    #def_amont = 1



    while (True):
        try:
            # Get user input
            item = input()
            # check if the item is in the dict for grocery
            if (item.title() in grocery_dict):
                # it is in the dict, add one item
                #print(item)
                #print(grocery_dict)
                grocery_dict[item.title()]= grocery_dict[item.title()]+1
            else:
                # add the item for the first time into the dict
                grocery_dict[item.title()] = 1


        except EOFError:
            # print in alphabetical order
            # print(grocery_dict)
            myKeys = list(grocery_dict.keys())
            myKeys.sort()
            sorted_dict = {i: grocery_dict[i] for i in myKeys}
            #print(sorted_dict)
            for item in sorted_dict:
                print(sorted_dict[item], item)
            break


main()


