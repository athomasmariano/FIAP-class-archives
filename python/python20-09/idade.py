print("Em que ano você nasceu?")
ano_nascimento = int(input())

idade = 2024 - ano_nascimento

# criterio de idadepara doar sangue: 16 a 69 anos
if idade <= 15 or idade >= 69:
    print("Você não pode doar sangue!")
elif idade == 16 or idade == 17:
    print("Você precida de autorização dos pais")
else:
    print("Você pode doar sangue!")
    
    