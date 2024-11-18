def menu_principal():
    """
    Exibe o menu principal e retorna a opção escolhida pelo usuário.
    """
    while True:
        print("\n---- Menu Principal ----")
        print("1. Inserir dados do usuário")
        print("2. Calcular economia")
        print("3. Ver resultados")
        print("4. Histórico de cálculos")
        print("5. Sair")
        opcao = input("Escolha uma opção: ")
        
        # Validação da opção escolhida
        if opcao in ['1', '2', '3', '4', '5']:
            return opcao
        else:
            print("Opção inválida! Por favor, escolha uma opção de 1 a 5.")

def coleta_dados():
    """
    Coleta dados do usuário sobre consumo, custo e localização.
    """
    while True:
        try:
            consumo = float(input("Digite seu consumo médio mensal em kWh (maior que zero): "))
            if consumo <= 0:
                raise ValueError("O consumo deve ser maior que zero.")
            
            custo_kwh = float(input("Digite o custo por kWh em sua região (maior que zero): "))
            if custo_kwh <= 0:
                raise ValueError("O custo por kWh deve ser maior que zero. Valores como 0.5 ou 0.92 são permitidos.")
            
            localizacao = input("Digite sua cidade e estado: ")
            return consumo, custo_kwh, localizacao
        except ValueError as e:
            print(f"Entrada inválida: {e}")


def calcula_economia(consumo, custo_kwh, rad_solar):
    """
    Calcula a economia mensal e anual com base nos dados fornecidos.
    """
    producao_estimada = rad_solar * 0.18 * 30  # Eficiência média de 18% e 30 dias
    economia_mensal = min(producao_estimada, consumo) * custo_kwh
    economia_anual = economia_mensal * 12
    return economia_mensal, economia_anual

def exibe_resultados(economia_mensal, economia_anual):
    """
    Exibe os resultados da economia mensal e anual.
    """
    print("\n---- Resultados ----")
    print(f"Economia mensal: R$ {economia_mensal:.2f}")
    print(f"Economia anual: R$ {economia_anual:.2f}")

def exibe_historico(historico):
    """
    Exibe o histórico de cálculos realizados.
    """
    if not historico:
        print("\n---- Histórico de Cálculos ----")
        print("Nenhum cálculo foi realizado ainda.")
    else:
        print("\n---- Histórico de Cálculos ----")
        for i, registro in enumerate(historico, start=1):
            consumo, custo_kwh, localizacao, economia_mensal, economia_anual = registro
            print(f"\nCálculo {i}:")
            print(f"Consumo: {consumo} kWh | Custo/kWh: R$ {custo_kwh:.2f} | Localização: {localizacao}")
            print(f"Economia Mensal: R$ {economia_mensal:.2f} | Economia Anual: R$ {economia_anual:.2f}")

def main():
    """
    Função principal que controla o fluxo do programa.
    """
    economia_mensal = economia_anual = 0  # Inicializamos com valores padrão
    rad_solar = 4.5  # Supondo uma radiação solar média
    historico = []  # Lista para armazenar o histórico de cálculos

    while True:
        opcao = menu_principal()

        if opcao == '1':
            consumo, custo_kwh, localizacao = coleta_dados()
            print("\nDados coletados com sucesso!")

        elif opcao == '2':
            try:
                if consumo and custo_kwh:
                    economia_mensal, economia_anual = calcula_economia(consumo, custo_kwh, rad_solar)
                    historico.append((consumo, custo_kwh, localizacao, economia_mensal, economia_anual))
                    print("\nCálculo de economia realizado com sucesso!")
                else:
                    print("\nPor favor, insira os dados do usuário primeiro (opção 1).")
            except NameError:
                print("\nErro: Você precisa inserir os dados do usuário primeiro (opção 1).")

        elif opcao == '3':
            if economia_mensal and economia_anual:
                exibe_resultados(economia_mensal, economia_anual)
            else:
                print("\nNenhum cálculo foi realizado ainda. Por favor, use a opção 2 para calcular economia.")

        elif opcao == '4':
            exibe_historico(historico)

        elif opcao == '5':
            print("\nSaindo do programa. Obrigado por usar nossa solução!")
            break

# Chama a função principal para iniciar o programa
main()
