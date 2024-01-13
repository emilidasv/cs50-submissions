def main():
    time = input("What time is it?")
    convert(time)



def convert(time):
     hours, minutes = time.split(":")
     min = round(minutes/60)
     print(min)

     if ((int(hours) >= 7)  and (int(hours) <= 8)) : print("breakfast time")
     elif ((int(hours) >=12) and (int(hours) <=13)) :print("lunch time")
     elif ((int(hours) >=18) and (int(hours) <=19)) : print("dinner time")


if __name__ == "__main__":
    main()
