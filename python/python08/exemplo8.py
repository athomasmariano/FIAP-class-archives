compras = []

print("Vamos criar a sua lista de compras!")
n = int(input("Quantos itens ela vai ter? "))

for i in range(n):
# Exercicio : Ler por input um item e salvar na lista de compras usando append
    item = input("Digite seu item: ")
    compras.append(item)
    
print(compras)