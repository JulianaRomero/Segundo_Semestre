import factorial as f



def comb():
    n = int(input("ingrese el numero de elementos"))
    m = int(input("ingrese el numero de elementos"))
    cmb = (f.factorial(n)/(f.factorial(m))*f.factorial(m-n))
    print(f"el numero de combinaciones posibles es: {cmb}")
    

if __name__=="__main__":
    comb()