lista = [1,2,3,4,5,6,7,8,9,10]
i = 0
impares = []
pares = []
while (i<=len(lista) - 1):
    if(lista[i]%2 == 0):
        impares.append(lista[i])
    else:
        pares.append(lista[i])
    i += 1

print(pares)
print(impares)