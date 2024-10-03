def fp(x,y,G):
    if len(G) == 1:
        if (  (x<=0 and y >=0) and not( (x-G[0])**2 + (y+G[0])**2 <= G[0]**2) and abs(x) <= G[0] and abs(y) <= G[0] ) or ( x>=0 and y <=0 and (x**2 + y**2 <= G[0]**2) ):
            # print(True,x, y, G[0])
            TF = True
        else:
            # print(False,x, y, G[0])
            TF = False
        return TF
    else:
        print("Некорректные геометрические параметры")
        return 404