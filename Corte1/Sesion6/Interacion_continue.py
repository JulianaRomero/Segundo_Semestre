n=int(input("Ingrese un numero: "))
i=0

while i<n:
    i+=1
    if i==4:
        print('freeze')
        continue
    print(i)