def main():
    due = 50
    print("Amount due:", due)
    while ( due > 0) :
        amount = input("Insert coin:")
        #print("Amount due:", calculate_new_due(due, amount))
        due = calculate_new_due(due, amount)
        print("Amount due:", due)


def calculate_new_due(due, amount):
    newdue = due - int(amount)

    return newdue



if __name__ == "__main__":
    main()
