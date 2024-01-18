import json
import requests
import sys
def main():
    if len(sys.argv) != 2:
        sys.exit()
    else:
        try:
            amount_of_bc = float(sys.argv[1])
        except:
            sys.exit()


    try:
        r = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
        #r.status_code
        #print(r.status_code)
        #print(r.text)
        #print("")
        #print("")
        #print(json.dumps(r.json(), indent=2))
        o = r.json()

        #for bpi in o["bpi"]:
            #print(bpi)
            #if (bpi =="USD"):
                #print("rate")
        #chosen_key = list(figlet_font_dict)[0]
        #chosen_val = list(figlet_font_dict.values())[0]
        bpi_dict = o["bpi"]
        #print(bpi_dict)
        chosen_val = list(bpi_dict.values())[0]
        rate = (chosen_val["rate_float"])
        #print(rate)

        amount = int(amount_of_bc) * float(rate)
        print(f"${amount:,.4f}")

    except requests.RequestException:
        ...


if __name__ == "__main__":
    main()
