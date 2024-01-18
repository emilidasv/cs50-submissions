import random
import sys


def main():


    size = get_level()
    #debug print(size)
    #debug print("A")
    if (size < 0):
        #debug print("Invalid")
        sys.exit("error")
    else:
        score = 0
        for i in range(0, 10):
            number_of_try = get_question(size)
            if number_of_try < 3:
                score = score+1
            #print("Score", score, "/10")
        print(score)



def get_question(size):
    x = generate_integer(size)
    y = generate_integer(size)
    question_str= str(x) + " + " + str(y) + " = "
    number_of_try = 0
    while True:
        if(number_of_try < 3):
            a = input(question_str)
            try:
                answer=int(a)
                correct_answer = x + y
                if answer!= correct_answer:
                    print("EEE")
                    number_of_try=number_of_try + 1
                else:
                    return number_of_try
            except ValueError:
                #sys.exit()
                return -1
        else:
            print(question_str, correct_answer)
            return number_of_try

def get_level():
    while True:
        size_of_number= input("")
        #debug print("B")
        try:
            #debug print("D")
            size = int(size_of_number)
            # debug print("E")
        except ValueError:
            #print("ValueError")
            #return -1
            #debug print("c")
            #sys.exit("Wrong argument")
            #return
            pass
        else:
            if size > 0 and size < 4:
                return size
            else:
                pass

def generate_integer(level):
    if level == 3: x = random.randint(100, 999)
    elif level == 2: x= random.randint(10, 99)
    else: x= random.randint(0, 10)
    return x

if __name__ == "__main__":
    main()
