# import csv
#import csv
# read csv file to a list of dictionaries
#with open('data_nutrition.csv', 'r') as file:
#    csv_reader = csv.DictReader(file)
#    data = [row for row in csv_reader]
#    for row in csv_reader:
#        print(row)



def main():
    fruit_dict = {"fruit": "calories",
            "Apple":  "130",
            "Avocado":  "50",
            "Banana":  "110",
            "Cantaloupe":  "50",
            "Grapefruit":  "60",
            "Grapes":  "90",
            "Honeydew ":  "50",
            "Melon":  "50",
            "Kiwifruit":  "90",
            "Lemon":  "15",
            "Lime":  "20",
            "Nectarine":  "60",
            "Orange":  "80",
            "Peach":  "60",
            "Pear":  "100",
            "Pineapple":  "50",
            "Plums":  "70",
            "Strawberries":  "50",
            "Sweet Cherries":  "100",
            "Tangerine":  "50",
            "Watermelon":  "80"}
    print(fruit_dict['Apple'])
    print(fruit_dict["Watermelon"])

    text = input("Item:")
    cal = fruit_dict[text]
    print("calories:",cal)


if __name__ == "__main__":
    main()
