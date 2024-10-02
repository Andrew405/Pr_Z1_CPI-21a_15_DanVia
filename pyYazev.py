from random import *
import module1
import matplotlib.pyplot as plt
global TF

# сохранение результатов 
log = open("test_log.txt", "r+")
def save_log(a,x,y):
    log.write(str(TF)+ "  " + str(x)+ "  " + str(y)+ "  " + str(r) + "\n")

for i in range(20):
    TF = 0
    x = randint(-40,40)
    y = randint(-40,40)
    r = randint(-40,40)

    # x,y, r = map(int, input().split()) #ручной ввод
    module1.fp(x,y,r)
    save_log(TF,x,y)
    i+=1

log.close()