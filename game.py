import random

def main():
    n= input("Level:")
    try:
        number_to_guess = random.randint(1,int(n))
    except ValueError:
        print("ValueError")


    while True :
        guess = input("Guess:")
        #print(number_to_guess)
        ##try:
        if int(guess) == number_to_guess:
            print ("Just right!")
            break
        elif int(guess) < number_to_guess:print("Too small!")
        else : print ("Too big!")
        ##except ValueError:
        ##print("ValueError")


if __name__ == "__main__":
    main()
