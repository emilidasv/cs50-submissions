def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    print(percent)
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    length = len(d)
    if d[0] == "$" :newd = d[1: length]
    return float(newd)


def percent_to_float(p):
    p_length = len(p)
    if p[p_length-1] == "%" :newp = p[0: p_length-1]
    pr=float(newp)
    pr=pr/100
    pr=float(pr)

    return pr

main()
