temperaturas = []
with open("dados.txt") as arquivo:
    for linha in arquivo:
        temperaturas.append(float(linha))
        
# TEMPERATURAS ALTAS
        
temperaturas_altas = []
for temperatura in temperaturas:
    if temperatura > 90:
        temperaturas_altas.append(temperatura)
        #print(temperaturas_altas)
        
    temperaturas_altas = [temperatura for temperatura in temperaturas if temperatura > 90]
    #print (temperaturas_altas)
    
# TEMPERATURA MUITO ALTAS
    
    temperaturas_muito_altas = []
for temperatura in temperaturas:
    if temperatura > 100:
        temperaturas_muito_altas.append(temperatura)
        #print(temperaturas_altas)
        
    temperaturas_muito_altas = [temperatura for temperatura in temperaturas if temperatura > 100]
    print (temperaturas_muito_altas)


'''PROPORÇÕES'''

# ALTAS

quantidade_temperaturas_altas = len (temperaturas_altas) 
quantidade_temperaturas = len (temperaturas)
print (quantidade_temperaturas_altas / quantidade_temperaturas)

# MUITO ALTAS

quantidade_temperaturas_muito_altas = len (temperaturas_muito_altas) 
quantidade_temperaturas = len (temperaturas)
print (quantidade_temperaturas_muito_altas / quantidade_temperaturas)