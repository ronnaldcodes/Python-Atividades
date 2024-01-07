# Faça um Programa que realize as operações matemáticas básicas.
def main():

    num1 = int(input('Digite um número: \n'))
    num2 = int(input('Agora digite outro: \n'))

    # A soma em python é representada pelo sinal de "+"
    print(f'A soma de {num1} + {num2} = {num1 + num2}')
    # A subtração em python é representada pelo sinal de "-"
    print(f'A subtração de {num1} - {num2} = {num1 - num2}')
    # A multiplicação em python é representada pelo sinal de "*"
    print(f'A multiplicação de {num1} x {num2} = {num1 * num2}')
    # A divisão em python é representada pelo sinal de "/"
    print(f'A divisão de {num1} / {num2} = {num1 / num2}')
    # A raiz quadrada em python, é representada pela multiplicação de um número, pela seguinte operação "(1/2)"
    print(f'A Raiz quadrada do {num1} e do {
          num2}, são respectivamente = {num1 ** (1/2)} e {num2 ** (1/2)}')
    # A potência de um número pelo outro, em python é representada pelo sinal de "**"
    print(f'A potência do {num1} elevado a {num2} = {num1**num2}')
    # O resto de um divisão em python é representada pelo sinal de "%"
    print(f'O resto da divisão de {num1} / {num2} = {num1 % num2}')

    return 0


if __name__ == "__main__":
    main()
