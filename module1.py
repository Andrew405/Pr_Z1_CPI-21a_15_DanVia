def fp(x,y,r):
    if ((x<=0 and y >=0) and not ( (x-r)**2 + (y+r)**2 <= r**2) and abs(x) <= r and abs(y) <= r ) or ( x>=0 and y <=0 and (x**2 + y**2 <= r**2) ):
        print(True,x, y, r)
        TF = True
    else:
        print(False,x, y, r)
        TF = False
    return TF