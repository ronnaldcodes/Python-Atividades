# Faça um Programa que leia um vetor(lista) de 5 números inteiros e mostre-os.
def main():

    i = 0

    lista = [10, 34, 12, 92, 8]

    for i in range(0, len(lista), 1):
        print(f"O item de indíce {i} da Lista é: {lista[i]}")

    return 0


if __name__ == "__main__":
    main()
