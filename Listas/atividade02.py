# Faça um Programa que leia 4 notas, mostre as notas e a média na tela.
def main():

    # Declaração de variáveis
    i = 0
    j = 0
    soma_notas = 0

    # Declaração de listas
    notas = []

    # Entrada de dados
    aluno = str(input("Digite o nome do aluno: \n").upper())

    # Validação de nome
    if (aluno != ""):
        # For para entrada dos dados da nota
        for i in range(1, 5, 1):
            nota = int(input(f"Digite a nota do {i} bimestre do aluno: \n"))
            notas.append(nota)
        print(notas)  # Saída da lista
        # For para somar as notas da lista
        for j in range(0, len(notas), 1):
            soma_notas += notas[j]
        # Print da média das listas
        print(f"A média do aluno {aluno}, foi de {soma_notas / 4}")

    return 0


if __name__ == "__main__":
    main()
