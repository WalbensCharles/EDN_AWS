def palindromo(texto):
    #tirar espaçó e puntuação
    texto=''.join(caratere for caratere in texto.lower() if caratere.isalnum())
    
 # Verificar se a string é igual de trás para frente
    return texto==texto[::-1]
while 1:
    palavra=input("digite uma palavra ou sair para( SAIR ) : ")
    if palavra.lower()=="sair":
        break

    if palindromo(palavra):
        print("sim")
    else:
        print("não")
    