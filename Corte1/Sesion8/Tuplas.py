def app(a,b,*args,**kwargs):
    print(kwargs)
    print(args)

if __name__=="__main__":
    app(1,2,5,7,9,2,3,6,3,7,6,5,3,6,7,34,23,35,x=1,m=2)
                                   