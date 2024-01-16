def main () :
    month_dict = {
    "January":1,
    "February":2,
    "March":3,
    "April":4,
    "May":5,
    "June":6,
    "July":7,
    "August":8,
    "September":9,
    "October":10,
    "November":11,
    "December":12
    }

    while (True):
        try:
            date_from_user = input("Date:")
            counter_of_comas = date_from_user.count(",")
            counter_of_slash = date_from_user.count("/")
            if counter_of_comas == 1:
                date_str_remove= date_from_user.replace(",", "")
                date_str = date_str_remove.split()
                #print("coma")
                #print(date_str)
                month_str= date_str[0]
                if month_str in month_dict:
                    month_number=month_dict[month_str]
                    if int(date_str[1]) <= 31 :
                        month_str = "{}-".format(str(month_number))
                        year_str="{}-".format(date_str[2])
                        new_str = year_str+month_str+date_str[1]
                        print(new_str)
            elif counter_of_slash == 2 :
                date_str2 = date_from_user.split("/")
                #print("slash")
                #print(date_str2)
                #print(date_str2[0])
                if date_str2[0].isdigit():
                    if ((int(date_str2[0]) <= 12 )
                        and (int(date_str2[1]) <= 31)):
                        #print(date_str2[2].rstrip(), "-".strip(),date_str2[0].rstrip(),"-",date_str2[1].rstrip())
                        year_str="{}-".format(date_str2[2])
                        month_str="{}-".format(date_str2[0])
                        new_str = year_str+month_str+date_str2[1]
                        print(new_str)
        except EOFError:
            break


#print(f"{n:02}")  leading zero


if __name__ == "__main__":
    main()
