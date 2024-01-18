import random


def main():

    while True:
        size_of_number= input("Level:")
        try:
            size = int(size_of_number)
            if size > 0 and size < 4:
                print("allok")

                x=random.rantint(0, 10*size)
                y=random.rantint(0, 10*size)
                problem = x  "+" y

                number_of_try=0
                not_yet_correct = True
                while not_yet_correct
                    a= input(problem)
                    try:
                        answer = int(a)
                        correct_answer = x+y
                        if answer != correct_answer : print("EEE")
                            number_of_try = number_of_try + 1
                    except ValueError:
                        print("ValueError")
                        break
        except ValueError:
            print("ValueError")
            break


def get_level():
    


def generate_integer(level):
    ...


if __name__ == "__main__":
    main()
