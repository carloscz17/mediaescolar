print("==================Menu=================")
print("= 1 - Desejo realizar uma consulta;   =")
print("==================Menu=================")

op = int(input("Digite sua opção: "))

while (op >= 0):
    soma = 0
    print("==================Menu=================")
    print("= 1 - Consultar media escolar;        =")
    print("= 0 - Sair                            =")
    print("==================Menu=================")
    op = int(input("Digite sua opção: "))
    if (op == 1):
        qnt = int(input("Informe a quantidade de notas que deseja fazer a média: "))
        soma = 0
        for i in range(qnt):
            numeros = float(input("Digite a sua nota :"))
            soma += numeros
        print("=======================================")
        media = soma/qnt
        if (media >= 0) and (media < 4):
            print("Provavelmente, você estará reprovado!")
        elif (media >= 4) and (media < 7):
            print("Provavelmente, você está na prova final!")
        elif (media >= 7) and (media <= 10):
            print("Parabéns, você está aprovado!")
        else:
            print("Média inválida!")
    print("=======================================")
    print("Sua média é:", media)
    print("=======================================")

    if (op == 0):
        print("Até a próxima!")
        break