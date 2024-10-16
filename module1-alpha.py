log = open("alpha_test_log.txt", "a")
def fp(x,y, R=10.):
    if (  (x<=0 and y >=0) and not( (x+R)**2 + (y-R)**2 <= R**2) and abs(x) <= R and abs(y) <= R ) or ( x>=0 and y <=0 and (x**2 + y**2 <= R**2) ):
        print(True,x, y, R)
        TF = True
        log.write("True" + " " + str(x) + " " + str(y) + " " + str(R) + "\n")
        return TF
    else:
        print(False,x, y, R)
        TF = False
        log.write("False" + " " + str(x) + " " + str(y) + " " + str(R) + "\n")
        return TF
x = float(input("X: "))
y = float(input("Y: "))
fp(x, y)