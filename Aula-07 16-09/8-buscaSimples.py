""" 8 - Dada a lista frutas = ["maçã", "banana", "laranja", "uva", "manga"], peça para o usuário
digitar uma fruta. Percorra a lista com for para verificar se a fruta digitada está presente e
exiba uma mensagem informando se foi encontrada ou não. """

def main():
    frutas = ["maçã", "banana", "laranja", "uva", "manga"]
    achou = False

    busca = input("Digite o nome de uma fruta: ").lower()

    for fruta in frutas:
        if(fruta == busca):
            print("A fruta está na lista!")
            achou = True

    if not achou:
        print("A fruta não está na lista.")

main()