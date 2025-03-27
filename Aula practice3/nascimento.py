#programa para calcular quatos dias de existençia na terra 

import datetime
def nasc(anos_nasc):
    ano_atual=datetime.datetime.now().year
    idade_atual=ano_atual-anos_nasc
    idade_dias =idade_atual*365
    return idade_dias

ano_nasc=int(input("digite seu ano de nascimento : "))
q_idade_em_dias=nasc(ano_nasc)

print(f"sua idade em dias é : {q_idade_em_dias} dias")

