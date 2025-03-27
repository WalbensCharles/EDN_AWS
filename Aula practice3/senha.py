#um programa par vericar senha forte

import string

def senha_forte(senha):
    """Verifica se a senha atende aos requisitos de segurança"""
    tem_tamanho = len(senha) >= 8
    tem_digito = any(char.isdigit() for char in senha)
    tem_maiuscula = any(char.isupper() for char in senha)
    tem_especial = any(char in string.punctuation for char in senha)  # Caracteres especiais

    return tem_tamanho and tem_digito and tem_maiuscula and tem_especial

def main():
    """Loop para solicitar uma senha forte ao usuário"""
    while True:
        senha = input("Digite uma senha forte (mínimo 8 caracteres, 1 número, 1 maiúscula e 1 caractere especial) ou 'sair' para terminar: ")
        
        if senha.lower() == "sair":
            print("Encerrando...")
            break
        
        if senha_forte(senha):
            print("Senha válida com sucesso! ✅")
            break
        else:
            print("Senha fraca. Tente novamente! ❌")

if __name__ == "__main__":
    main()
