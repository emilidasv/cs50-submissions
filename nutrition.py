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
            "apple":  "130",
            "avocado":  "50",
            "banana":  "110",
            "cantaloupe":  "50",
            "grapefruit":  "60",
            "grapes":  "90",
            "honeydew":  "50",
            "melon":  "50",
            "kiwifruit":  "90",
            "lemon":  "15",
            "lime":  "20",
            "nectarine":  "60",
            "orange":  "80",
            "peach":  "60",
            "pear":  "100",
            "pineapple":  "50",
            "plums":  "70",
            "strawberries":  "50",
            "sweet cherries":  "100",
            "wtangerine":  "50",
            "watermelon":  "80"}
#    print(fruit_dict['Apple'])
#    print(fruit_dict["Watermelon"])

    text = input("Item:")
    if text.lower() in fruit_dict:
        cal = fruit_dict[text.lower()]
        print("calories:",cal)


if __name__ == "__main__":
    main()
