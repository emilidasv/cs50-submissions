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
                # assign the day, month and year strings
                month_number_str = date_str[0]
                day_str = date_str[1]
                year_str = date_str[2]

                if month_number_str in month_dict:
                    month_number=month_dict[month_number_str]
                    month_number_str = str(month_number)
                    # add leading zero on day ans month
                    if (int(day_str) < 10): day_str = "0{}".format(day_str)
                    if (int(month_number_str) < 10): month_number_str = "0{}".format(month_number_str)

                    if int(day_str) <= 31 :
                        month_number_str = "{}-".format(month_number_str)
                        year_str="{}-".format(year_str)
                        new_str = year_str+month_number_str+day_str
                        print(new_str)
            elif counter_of_slash == 2 :
                date_str2 = date_from_user.split("/")
                #print("slash")
                #print(date_str2)
                #print(date_str2[0])

                # assign the day, month and year strings
                month_number_str = date_str2[0]
                day_str = date_str2[1]
                year_str = date_str2[2]
                # add leading zero on day ans month
                if (int(day_str) < 10): day_str = "0{}".format(day_str)
                if (int(month_number_str) < 10): month_number_str = "0{}".format(month_number_str)


                if month_number_str.isdigit():
                    if ((int(month_number_str) <= 12 ) and (int(day_str) <= 31)):
                        # add dashes
                        year_str="{}-".format(year_str)
                        month_number_str="{}-".format(month_number_str)

                        new_str = year_str+month_number_str+day_str
                        print(new_str)
        except EOFError:
            break


#print(f"{n:02}")  leading zero


if __name__ == "__main__":
    main()
