from random import *
import module1
import numpy as np

hits = 0
N = 1000 # количество выстрелов

# сохранение результатов 
log = open("test_log.txt", "r+")
def save_log(a,x,y):
    log.write(str(module1.fp(x, y, r))+ "  " + str(x)+ "  " + str(y)+ "  " + str(r) + "\n")

for i in range(N):
    TF = 0
    r = 30
    xm = np.round(np.random.uniform(-r-1/30*r, r+1/30*r, N),2)
    ym = np.round(np.random.uniform(-r-1/30*r, r+1/30*r, N),2)
# x,y, r = map(int, input().split()) #ручной ввод
for i in range(N):
        x = xm[i]
        y = ym[i]
        if (module1.fp(x,y,r)) == True:
            i+=1
            hits += 1
            save_log("True ",x,y)
        else:
             save_log("False ",x,y)
# область пристрелки x in range (-r-1/30*r, r+1/30*r) y in range (-r-1/30*r, r+1/30*r)


probability = hits / N

print(f"Количество выстрелов: {N}")
print(f"Количество попаданий: {hits}")
print(f"Вероятность попадания: {probability:.4f}")

log.close()