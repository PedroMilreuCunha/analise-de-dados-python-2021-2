def fact(x):
    """
    Função para calcular o fatorial de um número inteiro não-negativo

    param x: número inteiro não-negativo
    return: número inteiro não-negativo
    """
  # try/except para validação dos inputs
    try:
        x = int(x)
        if x < 0:
            print(f'Erro: o número não pode ser negativo')
        else:
            resultado = 1
            for i in range(x, 1, -1):
                resultado *= i
            return print(f"O fatorial de {x} é {resultado}.")
    except:
        print(f"Erro: {x} não é um número inteiro.")