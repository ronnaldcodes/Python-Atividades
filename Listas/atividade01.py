# Faça um Programa que leia um vetor de 10 números reais e mostre-os na ordem inversa.
def main():

    # declarando variáveis de controle
    i = int(0)
    j = int(0)

    # declarando listas
    numeros = []
    lista_contrario = []

    # loop de controle
    for i in range(0, 10, 1):
        lista = int(input("Digite um número: \n"))  # entrada de dados
        numeros.append(lista)  # processamento

    print(f"Lista normal: {numeros}")  # saída de dados

    # saída de dados - Forma 1
    # Aqui utlilizaremos o "len(numeros) - 1", pelo fato de que sem ele, estariamos acessando o último elemento da lista duas vezes
    for j in range(len(numeros) - 1, -1, -1):
        lista_contrario.append(numeros[j])
    print(f"Lista invertida 01: {lista_contrario}")
    # saída de dados - Forma 2
    print(f"Lista invertida 02: {numeros[::-1]}")
    # saída de dados - Forma 3
    numeros.reverse()
    print(f"Lista invertida 03: {numeros}")

    return 0


if __name__ == "__main__":
    main()
