import datetime

data = datetime.datetime.now() 
ano_atual = data.year
mes_atual = data.month
dia_atual = data.day


print("Em que ano você nasceu?")
ano_nascimento = int(input())


idade_maxima = ano_atual - ano_nascimento

print("Estamos no ano:", ano_atual)
print("Portanto você fez ou fará", idade_maxima, "anos este ano")

mes_aniversario = int(input("Qual o mês do seu aniversário? (1-12)"))
dia_aniversario = int(input("Qual é o dia do seu aniversário? (1-30)"))

if mes_aniversario < mes_atual:
    print("Você já fez aniversário esse ano!\n")
    idade_real = idade_maxima
elif mes_aniversario == mes_atual and dia_aniversario <= dia_atual:
    print("Você já fez aniversário esse ano!\n")
    idade_real = idade_maxima
else:
    print("Você ainda não fez aniversário esse ano!\n")
    idade_real = idade_maxima - 1
print("Então você tem", idade_real, "anos de idade.\n")
    
    