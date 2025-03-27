#programa para calcula ano bissexto

#processamento
def bissexto(ano):
    
    if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
        return True
    else:
        return False
#entrada
ano = int(input("Digite um ano: "))

#saida
if bissexto(ano):
    print(f"{ano} é um ano bissexto!")
else:
    print(f" O ano {ano} não é um ano bissexto.")
