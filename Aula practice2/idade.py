# programinha para verifica idades dos ciclos1212 da vida
idade=int(input("digite a sua idade : "))
#verificação das idades e as saidas conforme as idades
if idade<= 12 :
    print("Criança")
elif idade > 12 and idade <=17:
    print("adolescente")

elif idade >= 18 and idade < 60 :
    print("adulto")
else:
    print("idoso")
