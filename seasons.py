from datetime import datetime, date
from dateutil import parser
import inflect
import sys
import re

def main():
    date_in_text = input("Date of Birth:")


    if matches := re.search(r'([1-2][9|0][0-9][0-9])-(0[1-9]|1[0-2])-(0[1-9]|1[0-9]|2[0-9]|3[0-1])', date_in_text):
        print(matches.group())
    else:
        sys.exit("Invalid date")
    minutes = calculate_minutes(date_in_text)


    p = inflect.engine()
    output_str = p.number_to_words(minutes, andword=",") + " minutes"
    print(output_str)


def calculate_minutes(date_in_text):
    date_format = "%Y-%m-%d"
    # todays date
    today_str= str(date.today())
    #print(today_str)
    today_obj = datetime.strptime(today_str,date_format )
    date_in_obj = datetime.strptime(date_in_text, date_format)
    #print(type(today_obj))
    #print(type(date_in_obj))
    days_difference = today_obj - date_in_obj
    #print(days_difference)
    #print(days_difference.total_seconds())
    minutes = int(days_difference.total_seconds()/60)
    #print(int(minutes))
    print(minutes)

    return minutes


if __name__ == "__main__":
    main()
