def cumprimenta(nome):
    # nome é uma variável que podemos usar dentro da função
    # o valor dela será definida na chamada
    print("Bom dia", nome)
    
    
cumprimenta("João") # Chama a função
cumprimenta("Aline")

nome = input("Qual o seu nome?")
cumprimenta(nome)