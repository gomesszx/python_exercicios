a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())
f = int(input())
g = int(input())
h = int(input())
i = int(input())
j = int(input())
lista = [a,b,c,d,e,f,g,h,i,j]
    
i = 0
impares = []
pares = []
while (i<=len(lista) - 1):
    if(lista[i]%2 == 0):
        impares.append(lista[i])
    else:
        pares.append(lista[i])
    i += 1

print(impares)
print(pares)