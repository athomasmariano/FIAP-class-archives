def exemplo():
    x = 5 # Essa é outra variável, que só existe no escopo da função
    
def funcao():
    print("Esta é uma função")
    
def main():
    print("O programa está começando...")
    x = 3
    exemplo()
    print(x)
    
# if __name__ == 'main':
    main()
    
    # Todas as linhas qe ão está dentro de função são executadas
    # (Na ordem que estão escritas)

main()



