produtos = {
}

for _ in range(5):
    produto = input("Produto:")
    preco_prod = float(input("Preco:"))

    produtos[produto] = preco_prod

for produto in produtos:
     if (produtos[produto] > 50):
         print(produto)


