import re
import sys


def main():
    print(convert(input("Hours: ")))
#input format:
#9:00 AM to 5:00 PM
#9 AM to 5 PM


def convert(text):
    text = text.strip()
    output=''
    if matches := re.search(r'^(([0-9][0-2]?):?([0-5][0-9]?)?) ([A|P]M) to (([0-9][0-2]?):?([0-5][0-9]?)?) ([A|P]M)$', text, re.IGNORECASE):

        tmpoutput= matches.groups()
        begin_hours_str = matches[2]
        begin_min_str = matches[3]
        if begin_min_str == None: begin_min_str =""
        end_hours_str= matches[6]
        end_min_str= matches[7]
        if end_min_str == None: end_min_str =""
        begin_hours_int=int(begin_hours_str)
        end_hours_int=int(end_hours_str)

        #print(begin_hours_str)
        #print(begin_min_str)
        #print(end_hours_str)
        #print(end_min_str)

        #print(matches.groups())

        if begin_hours_int<12 and str(matches.group(4))=="PM":
            begin_hours_str = str(begin_hours_int + 12)
        elif begin_hours_int == 12 and str(matches.group(4))=="AM":
            begin_hours_str="00"
        #else:
        #     print("else")
        if begin_min_str =="" :
            begin_output = begin_hours_str + begin_min_str
        else:
            begin_output = begin_hours_str + ":" + begin_min_str

        if end_hours_int<12 and str(matches.group(8))=="PM":
            end_hours_str = str(end_hours_int + 12)
        elif end_hours_int == 12 and str(matches.group(4))=="AM":
            end_hours_str="00"
        #else:
            #print("else")

        if end_min_str =="" :
            end_output = end_hours_str +  end_min_str
        else:
            end_output = end_hours_str + ":" + end_min_str



        output= begin_output + " to " + end_output

    else:
        output = "None"
        #print(type(output))

        #print("None")
    #print(matches)

    return output


if __name__ == "__main__":
    main()

