def main():
    menu_dict={
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
    }

    total_amount= 0
    while (True):
        try:
            item = get_ans("Item:")
            if (item.title() in menu_dict):
                price = menu_dict[item.title()]
                total_amount= total_amount + price
                #print(total_amount)
        except EOFError:
            print("Total:", total_amount)
            break



    #print(f"x is {x}")


def get_ans(prompt):
    while True:
        try:
            return input(prompt)
        except ValueError:
            pass


main()
