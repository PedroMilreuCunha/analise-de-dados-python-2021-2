from funcoes import fatorial, media_aritmetica, media_geometrica

while True:
    operacao = int(input("Qual operação você deseja realizar?\
    \n \t 1 - Média aritmética (n valores)\
    \n \t 2 - Média geométrica (2 valores)\
    \n \t 3 - Fatorial (1 valor)\n"))
    if operacao not in [1, 2, 3]:
        print("Opção inválida!")
    elif operacao == 1:
        numeros = []
        contador = 1
        while True:
            entrada = input(f"Digite o {contador}º número ou 'Q' para finalizar a entrada.\t")
            if entrada.upper() == 'Q':
                break
            else:
                numeros.append(float(entrada))
                contador += 1
        print(f"A média aritmética dos valores digitados é: {media_aritmetica.ma(numeros)} ")
        break
    elif operacao == 2:
        numeros = []
        for i in range(2):
            numeros.append(float(input(f"Digite o {i+1}º número.\t")))
        if numeros[0]*numeros[1] < 0:
            print("Não existe raiz quadrada de valores negativos nos números reais.")
        else:
            print(f"A média geométrica dos valores digitados é: {media_geometrica.mg(numeros[0], numeros[1])}")
            break
    elif operacao == 3:
        numero = input("Digite o número inteiro para o qual você deseja saber o fatorial (Ex. 5! = 120).\t")
        fatorial.fact(numero)
        break