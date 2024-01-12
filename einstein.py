def main():
   m = input("m:")
   print(m)

   E = calculate_E(m)
   print("E:", calculate_E(m))

def calculate_E(p):
    c = 300000000
    E= c*c*int(p)
    return E
main()
