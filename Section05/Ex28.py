""" Faça um programa que leia três números inteiros positivos e efetue o cálculo
de uma das seguintes médias de acordo com um valor numérico digitado pelo usuário:
(A) Geométrica; (B) Ponderada; (C) Harmônica; (D) Aritmética.
"""


mediaEscolhida = input("Escolha o tipo de média => "
                       "\n(A) Geométrica;"
                       "\n(B) Ponderada;"
                       "\n(C) Harmônica;"
                       "\n(D) Aritmética;"
                       "\n Resposta: ").upper()

if mediaEscolhida == 'A' or mediaEscolhida == 'B' or mediaEscolhida == 'C' or mediaEscolhida == 'D':
    valorX = int(input("\nDigite o primeiro valor (número inteiro positivo): "))
    valorY = int(input("Digite o segundo valor (número inteiro positivo): "))
    valorZ = int(input("Digite o terceiro valor (número inteiro positivo): "))

    if valorX >= 0 and valorY >= 0 and valorZ >= 0:
        print("\n__________________________________________________\n")
        if mediaEscolhida == 'A':
            resposta = (valorX * valorY * valorZ) ** (1 / 3)
            print(f"A média geométrica destes três números: {valorX}, {valorY} e {valorZ} é igual a : {resposta}\n")


        if mediaEscolhida == 'B':
            resposta = (valorX + 2 * valorY + 3 * valorZ) / 6
            print(f"A média ponderada destes três números: {valorX}, {valorY} e {valorZ} é igual a : {resposta}\n")


        if mediaEscolhida == 'C':
            resposta = 1 / (1 / valorX) + (1 / valorY) + (1 / valorZ)
            print(f"A média harmônica destes três números: {valorX}, {valorY} e {valorZ} é igual a : {resposta}\n")


        if mediaEscolhida == 'D':
            resposta = (valorX + valorY + valorZ) / 3
            print(f"A média aritmética destes três números: {valorX}, {valorY} e {valorZ} é igual a : {resposta}\n")


    else:
        print("\n__________________________________________________\n")
        print("Você digitou um número negativo! Tente novamente.")

else:
    print("\n_________________________")
    print("\nEscolha uma opção válida")