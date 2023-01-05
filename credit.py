# TODO
from cs50 import get_string


def main():

    input_is_numbers = False
    # prompt for input of creit card number
    creditnumber = get_creditcardnumber()

    # calculate lenth of creditcard number
    length = len(creditnumber)

    # calculate checksum
    checksum = calculate_checksum(creditnumber, length)

    # todo
    firstnum = int(creditnumber[0])
    secondnum = int(creditnumber[1])
    status1 = valid_cardandTypeofcard(firstnum, secondnum, length)

    # check if checksum is valid
    if ((checksum % 10) != 0) or (status1 == 0):
        print("INVALID")
    else:
        if status1 == 3:
            print("AMEX")
        elif status1 == 4:
            print("VISA")
        elif status1 == 5:
            print("MASTERCARD")


def get_creditcardnumber():
    while True:
        try:
            # prompt for input of creit card number
            cnum = get_string("Give me credit number")
            n = int(cnum)
            if n > 0:
                return cnum
        except ValueError:
            cnum = "Error"


def calculate_checksum(cnum, len):
    sumeven = 0
    sumodd = 0
    tmpnum = cnum
    j = len - 1
    k = 1
    for i in range(len):

        # number in string
        tmpnum = cnum[j]
        digit = int(tmpnum)
        # number from end of card

        if (k % 2) != 0:

            sumeven = sumeven + digit
        else:
            digit = digit * 2
            if (digit < 10):
                sumodd = sumodd + digit
            else:
                sumodd = sumodd + 1 + (digit - 10)
        k += 1
        j -= 1
    return sumeven + sumodd


def valid_cardandTypeofcard(frstnum, secnum, len):
    # heck if card number fullfill requireent for AMEX , Mastercard or VISA
    # VISA: starts with 4  - AND -  13 or 16 digits
    # Master Card: starts with 51,52,53,54,55  - AND - 16 digits
    # American Express: starts with 34 or 37 - AND - 15 digits
    if (frstnum == 4) and ((len == 13) or (len == 16)):
        return 4
    elif (frstnum == 3) and ((secnum > 0) or (secnum < 6)) and (len == 15):
        return 3
    elif (frstnum == 5) and ((secnum > 0) or (secnum < 6)) and (len == 16):
        return 5
    else:
        return 0


main()

