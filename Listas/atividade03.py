# Faça um Programa que leia um vetor de 10 caracteres, e diga quantas consoantes foram lidas. Imprima as consoantes.

def main():

    # declaração de variável de controle
    consoantes = 0
    # declarando o vetor
    nomes = ["Alex", "Beatriz", "Cassia", "Daniel", "Eduarda",
             "Fabiano", "Gabriella", "Hugo", "Iago", "Joseph"]

    # repetição selecionando cada item da lista
    for i in range(0, len(nomes), 1):
        novo_nome = ""  # declarando variável substituta
        novo_nome2 = ""  # declarando variável substituta

        # Comparando cada letra de um nome com o "A"
        for j in range(0, len(nomes[i]), 1):
            if ((nomes[i])[j].upper() != "A"):
                # A variável novo_nome recebe cada letra que não seja a vogal "A"
                novo_nome += (nomes[i])[j]

        # Comparando cada letra de um nome com o "E"
        for k in range(0, len(novo_nome), 1):
            if (novo_nome[k].upper() != "E"):
                # A variável novo_nome2 recebe a palavra sem a vogal "E"
                # A variável novo_nome2 recebe cada letra que não seja a vogal "E"
                novo_nome2 += novo_nome[k]
        novo_nome = ""  # Zerando a variável novo_nome, para que ela receba um novo valor

        # Abaixo o padrão segue o mesmo e a única mudança é na Vogal

        for l in range(0, len(novo_nome2), 1):
            if (novo_nome2[l].upper() != "I"):
                novo_nome += novo_nome2[l]
        novo_nome2 = ""

        for m in range(0, len(novo_nome), 1):
            if (novo_nome[m].upper() != "O"):
                novo_nome2 += novo_nome[m]
        novo_nome = ""

        for n in range(0, len(novo_nome2), 1):
            if (novo_nome2[n].upper() != "U"):
                novo_nome += novo_nome2[n]
        # Substituindo o nome que está na lista, pelo novo nome sem vogal
        nomes[i] = novo_nome
        # Contando as consoantes
        consoantes += len(novo_nome)

    # Saída de dados
    print(nomes)
    print(consoantes)

    return 0


if __name__ == "__main__":
    main()
