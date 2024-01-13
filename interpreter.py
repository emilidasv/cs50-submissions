expr = input("Expresseion:")
expre_array= expr.split(" ")
#print(expr)
#print(expre_array)
#print(len(expre_array))
x = expre_array[0]
y = expre_array[2]
constr = expre_array[1]
string = x + constr + y
p =round(eval(string),1)/10
p = p *10
print(p)

