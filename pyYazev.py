from random import *
import module1
import numpy as np
import pandas as pd
import openpyxl

hits = 0
N = 50 # количество выстрелов

# сохранение результатов 
log = open("test_log.txt", "w+")
def save_log(a,x=None,y=None):
    if x == None and y == None:
        log.write("Некорректные геометрические параметры")
    else:
        log.write(str(module1.fp(x, y, G))+ "  " + str(x)+ "  " + str(y)+ "  " + str(G[0]) + "\n")

G = []
print("Выберите режим: ")
print("1. Основной режим")
print("2. Два радиуса (некорректные геометрические параметры)")
print("3. Радиус и две стороны (некорректные геометрические параметры)")    # Выбор режима ввода данных
choice = int(input())

print("Введите желаемые параметры: ")
for i in range(choice):
    G.append(int(input()))
G = tuple(G)

for i in range(N):
    TF = 0
    xm = np.round(np.random.uniform(-G[0]-1/30*G[0], G[0]+1/30*G[0], N),2)
    ym = np.round(np.random.uniform(-G[0]-1/30*G[0], G[0]+1/30*G[0], N),2)
# x,y, r = map(int, input().split()) #ручной ввод

for i in range(N):
        x = xm[i]
        y = ym[i]
        if module1.fp(x, y, G) == 404:
            save_log("Некорректные геометрические параметры")
            break
        elif (module1.fp(x,y,G)) == True:
            i+=1
            hits += 1
            save_log("True ",x,y)
        else:
            save_log("False ",x,y)
# область пристрелки x in range (-r-1/30*r, r+1/30*r) y in range (-r-1/30*r, r+1/30*r)

A = []
A.insert(0, ["№", "X", "Y", "P"])
for i in range(N):
    x = xm[i]
    y = ym[i]
    A.append([int(i+1), float(x), float(y), module1.fp(x, y, G)])
# print(A)
AMatr = np.matrix(A)
# print(AMatr)    #Создание Матрицы numpy

B = []
B.insert(0, ["X", "Y", "P"])
for i in range(N):
    x = xm[i]
    y = ym[i]
    B.append([float(x), float(y), module1.fp(x, y, G)])
# print(B)
BMatr = pd.DataFrame(B)
print(BMatr)

pd.DataFrame(B).to_csv('BMatr.csv', header= False, index= False, sep= ';', decimal= 2)
pd.read_csv('BMatr.csv', parse_dates= False)
pd.DataFrame(B).to_excel('BMatr.xlsx', index= False, header= False)    # Вывод Датафрейма в .csv и .xlsx файлы

probability = (hits / N)*100

print(f"Количество выстрелов: {N}")
print(f"Количество попаданий: {hits}")
print(f"Вероятность попадания: {probability:.2f}%")

log.close()