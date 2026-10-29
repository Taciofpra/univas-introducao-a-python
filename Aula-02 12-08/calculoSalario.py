#7. Cálculo de Salário
#- Crie um programa que pergunte quanto o usuário ganha por hora e o número de horas trabalhadas no mês. 
#  Calcule e mostre o total do salário referido mês.

def main():
    hSalario = float(input("Digite seu salario por Hora: "))
    horas = float(input("Digite as horas trabalhadas no mes: "))

    salario = hSalario * horas

    print("Salario desse mês: ", salario)

main()