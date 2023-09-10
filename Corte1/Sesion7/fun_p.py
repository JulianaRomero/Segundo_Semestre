import fun_suma

def main():
    a = int(input("ingrese un numero"))
    b = int(input("ingrese un numero"))
    r = fun_suma.sum(a,b)
    print(r)
    print(f"ejecutado desde {__name__}")




if __name__=="__main__":
    main()