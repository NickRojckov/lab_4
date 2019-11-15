import random
n = int(input("Введите размер списка:\n"))
X = []
for i in range(n):
    a = random.randint(0,100)
    X.append(a)    
for i in range(n):
    print(X[i])
for i in X:
    if i % 3 == 0:
        X.remove(i)
        print(X[i])
