def main():
    salario = float(input("Digite seu salário: "))
    reajuste = float(input("Digite o percentual de reajuste: "))

    novoSalario = salario * (reajuste/100 + 1)
    print("Valor do reajuste: %.2f"% (novoSalario - salario))
    print("Novo Salário: %.2f"% novoSalario)

main()

