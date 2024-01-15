item=input("Item:")

total_amount= 0
do_continue = True

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

while (do_continue):
    try:
        if (item.title() in menu_dict):
            price = menu_dict[item.title()]
            total_amount= total_amount + price
            print("Total:", total_amount)
            item=input("Item:")
    except EOFError:
        do_continue = False

print("Total:", total_amount)

