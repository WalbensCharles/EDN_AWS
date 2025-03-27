#programa para consulta CEP 
import requests

def consulta_cep(cep):
    url= f"https://viacep.com.br/ws/{cep}/json/"
    try:
        resposta =requests.get(url)
        resposta.raise_for_status() #verificar se houve um erro na requisição
        dados=resposta.json()

        if "erro" in dados:
            return "CEP não encontrado."
        
        return f"""
        CEP:{cep}
        LOGARDOURO: {dados.get('logradouro','nao informado')}
        BAIRRO :    {dados.get('bairro','nao informado')}
        CIDADE :    {dados.get('localidade','nao informado')}
        ESTADO :    {dados.get('uf','nao informado')}
        """

    except  requests.RequestException as e:
         return f"Erro na consulta: {e}"
    
def main():
    d_cep=input("digite um cep valido (somente números) : ")
    print("estamos consultando o cep aguarde ..............")

    resultado=consulta_cep(d_cep)
    print(resultado)
if __name__ =="__main__":
    main()