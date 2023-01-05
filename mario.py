# TODO
from cs50 import get_int


def main():

    height = get_height()
    width = 1
    for i in range(height):
        for i in range(height-width):
            print(" ", end="")
        print("#" * width)
        width += 1


def get_height():
    while True:
        n = get_int("Height: ")
        if n > 0 and n < 9:
            return n


# comments
# run the main program


main()
