#Faça um Programa que peça o raio de um círculo, calcule e mostre sua área.

def main():

    #declarando variáveis
    pi = 3.1415

    #entrada de dados
    raio = float(input("Digite o raio do círculo: \n"))

    #processamento de dados
    area = (raio**2) * pi

    #saída de dados
    print(f"A área do cículo é: {area}")

    return 0
if __name__ == "__main__":
    main()