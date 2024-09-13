'''

Este programa lê o nome e sobrenome do usuário e o cumprimenta

'''

print ("Qual o seu nome?")
nome = input()

print("Qual o seu sobrenome?")
sobrenome = input()

print("Olá", nome, sobrenome)

print("Em que ano você nasceu?")
ano_nascimento = int(input())

if ano_nascimento <- 2000 and ano_nascimento >= 1900:
    print("Você nasceu no século XX")
elif ano_nascimento >= 2001 and ano_nascimento <= 2100:
    print("Você nasceu no século 21")
else:
    print("...sério?")  
    
    