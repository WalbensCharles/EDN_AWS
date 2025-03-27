#calculadora para calcular massa de corpo e imforme os resultados

# entradas 
peso=int(input("digite seu peso : "))
altura=int(input("digite seu peso : "))
#processamento
imc=altura /(peso**2)
#Verificação de pesos
if imc < 18.5:
    print("abaixo do peso ")
elif  imc <25:
    print("peso normal")
elif   imc <38:
    print("sobre peso")
else:
    print("obeso")
print(f"seu imc {imc:.2f} tomar cuidado hein !")    