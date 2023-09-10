import random as r

def app():
    pal = ""
    nombre = "hola mundo"
    while pal != "exit":
        x = r.randint(100,180)
        #x = r.uniform(100,180)
        #x = r.choice(nombre)
        print(x)
        pal = input("para salir escriba exit")

if __name__=="__main__":
    app()