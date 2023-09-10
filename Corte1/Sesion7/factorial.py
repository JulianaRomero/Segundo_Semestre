

def factorial(x):
    a = 1
    for i in range(1,4):
        a = a*i #a=a *i
        print(a)
    print(f"resultado {a}")

if __name__=="__main__":
    factorial(4)