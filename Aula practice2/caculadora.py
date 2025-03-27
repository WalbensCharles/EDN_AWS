#programa calculadora para fazer calcular simples e tratar de erro de digitação
while(1):
    try :
        

        nu1=int(input("digite um numero : "))
        nu2=int(input("digite o segundo numero : "))
        op=input("digite uma operacao valida (+ ,/ ,- ,* ) ")

        if op =="+":
            resu=nu1+nu2
        elif op =="-":
            resu= nu1-nu2

        elif op=="*":
            resu=nu1*nu2

        elif op=="/":
            if nu2==0:
                raise ZeroDivisionError("Não e possivel a divisão por zero")
            resu= nu1/nu2

        else :
            raise ValueError("operacao invalida, digite um operação valido por favor")
        print(f"o resultado : {resu}")
        break

  

    except ValueError as e:
        print(f"erro : {e} tente novamente")
    except ZeroDivisionError as e:
        print(f"Erro {e} tente novamente")
        