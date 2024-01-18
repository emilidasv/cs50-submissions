import random

def main():
    n= input("Level:")
    number_to_guess = random.randint(1,int(n))
    while True :
        guess = input("Guess:")
        print(number_to_guess)
        if int(guess) == number_to_guess:
            print ("Just right!")
            break
        elif int(guess) < number_to_guess:print("Too small!")
        else : print ("Too big!")


if __name__ == "__main__":
    main()
