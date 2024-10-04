texto1 = "bom dia"
texto2 = "bom dia, estamos na aula de computional thinking"

for caractere in texto1:
    print(caractere)
espacos = 0
for caractere in texto2:
    if caractere == " ":
        espacos += 1
print("O texto2 tem", espacos, "espaços")

        
# Modifique esse código para contar quantas letras "a"  
        
contador = 0

print("\n---------\n")

for caractere in texto2:
    if caractere == "a":
        contador += 1
        
print("O texto2 tem", contador, "a's" )    