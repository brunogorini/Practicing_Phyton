# Ocorrências de palavras num texto
# Autor: Bruno Gorini

# Esse programa contabiliza a ocorrência de cada palavra de um conjunto num dado discurso.

# Entrada:
# Um arquivo de texto contendo um conjunto de palavras e outro contendo um discurso.

# Saída:
# Um arquivo texto contendo o número de ocorrências de cada palavra do conjunto no discurso informado.

# Obs: O discurso exemplo foi escrito respeitando o tamanho máximo da linha e a aplicação das regras de translineação.



# Programa Completo

# Subprogramas


def ler_palavras():
    arq_palavras = open('palavras.txt', 'r')
    conjunto_palavras = set()
    palavra = arq_palavras.readline()
    palavra = palavra.replace('\n', '')
    conjunto_palavras.add(palavra)
    while palavra != '':
        palavra = arq_palavras.readline()
        palavra = palavra.replace('\n', '')
        conjunto_palavras.add(palavra)
    conjunto_palavras.discard('')
    arq_palavras.close()
    return conjunto_palavras


def ler_discurso():
    arq_discurso = open('discurso.txt', 'r')
    linhas_discurso = arq_discurso.readlines()
    for linha in range(len(linhas_discurso) - 1):
        linhas_discurso[linha] = linhas_discurso[linha].replace('\n', '')
    string_discurso = str.join(' ', linhas_discurso)
    string_discurso = string_discurso.replace('- ', '')
    arq_discurso.close()
    return string_discurso


def criar_dic(conjunto_palavras, string_discurso):
    dic_contagem = dict()
    vetor_discurso = string_discurso.split(' ')
    for word in conjunto_palavras:
        contagem = 0
        for string in range(len(vetor_discurso)):
            if word == vetor_discurso[string]:
                contagem += 1
        dic_contagem[word] = str(contagem)
    return dic_contagem


def print_contagem(dic_contagem):
    arq_contagem = open('contagem.txt', 'w')
    for key, value in dic_contagem.items():
        arq_contagem.write(key + ' ' + value + '\n')
    arq_contagem.close()
    return None


# Programa Principal

palavras = ler_palavras()
discurso = ler_discurso()
dicionario = criar_dic(palavras, discurso)
print_contagem(dicionario)
