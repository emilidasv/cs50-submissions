def main():
    time = input("What time is it?")
    convtime = convert(time)
    if (convtime >= 7)  and (convtime <= 8) : print("breakfast time")
    elif (convtime>=12) and (convtime <=13) :print("lunch time")
    elif (convtime >=18) and (convtime <=19) : print("dinner time")
    else:
        print("")

def convert(time):
     hours, minutes = time.split(":")
     min = int(minutes)/60
     x = int(hours)+min
     return x



if __name__ == "__main__":
    main()
