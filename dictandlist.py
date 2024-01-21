def main():

    my_dict = {"name":"Carolina", "efternamn":"nilsson"}
    print("mydict", my_dict)
    mylist_if_dict= []
    mylist_if_dict_keys=list(my_dict.keys())
    print("mylist_if_dict", mylist_if_dict_keys)
    mylist_if_dict_keys.append(list((my_dict["name"] ,":", my_dict["efternamn"])))
    print("mylist_if_dict", mylist_if_dict_keys)









if __name__ == "__main__" :
    main()
