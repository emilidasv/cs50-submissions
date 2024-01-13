def main():
    time = input("What time is it?")
    convert(time)



def convert(time):
     hours, minutes = time.split(":")
     min = int(minutes)/60
     print(min)
     time=hours+min

     if ((int(hours) >= 7)  and (int(hours) <= 8)) : print("breakfast time")
     elif ((int(hours) >=12) and (int(hours) <=13)) :print("lunch time")
     elif ((int(hours) >=18) and (int(hours) <=19)) : print("dinner time")

return print(hours+min)

if __name__ == "__main__":
    main()
