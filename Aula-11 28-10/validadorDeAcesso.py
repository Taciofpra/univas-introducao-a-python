""" Enunciado: Crie uma função chamada verificar_senha que receba uma string digitada 
pelo usuário. Se a string for igual a "SI2026", a função deve retornar True. Caso
 contrário, deve retornar False. Fora da função, use um if/else para exibir 
"Acesso Concedido" ou "Acesso Negado" com base no retorno. """

def verificar_senha(Senha):
    if(Senha == "SI2026"):
        return True
    else:
        return False
    

def main():
    verificador = False
    while not verificador:
        senha = input("Digite a senha: ")
        verificador = verificar_senha(senha)
        if(not verificador):
            print("Senha incorreta!, Acesso negado! tente novamente.")
        else:
            print("Acesso permitido!")

main()