# Corretor de digitação repetida
# Autor: Bruno Gorini

# Mensagens são informadas a partir de um arquivo texto de entrada e a resposta em um arquivo texto de saída.

# A primeira linha do arquivo de entrada indica a quantidade N de mensagens.

# LIMITAÇÕES:
# Mensagens não devem incluir pontuação.
# Todas as palavras são compostas por letras minúsculas, sem acento e sem cedilha.
# Mensagens não devem incluir palavras que naturalmente são compostas por repetições no final,como “banana” e “arara”.

#SAÍDA:
# O programa escreve N linhas no arquivo de saída.
# Cada linha contém a quantidade de palavras corrigidas e a versão corrigida da mensagem de entrada.


# Programa Completo

# Subprogramas


def separar_palavras(sentenca):
    lista_palavras = sentenca.split(' ')
    lista_palavras[len(lista_palavras) - 1] = lista_palavras[len(lista_palavras) - 1].replace('\n', '')
    return lista_palavras


def remove_repeat(lista_palavras):
    sentence_correct = []
    count = 0
    for palavra in lista_palavras:
        meio = int(len(palavra) / 2)
        for i in range(len(palavra) - 1):
            for j in range(meio, len(palavra)):
                if palavra[i:j] == palavra[j:]:
                    palavra = palavra[:j]
                    count += 1
        sentence_correct.append(palavra)
    return sentence_correct, count


# Programa Principal

dados = open('mensagens_originais.txt', 'r')
N = int(dados.readline())
msgs_corrigidas = []

for frase in range(N):
    linha = dados.readline()
    frase_corrigida, contagem = remove_repeat(separar_palavras(linha))
    frase_corrigida.insert(0, str(contagem))
    msgs_corrigidas.append(frase_corrigida)

dados.close()

dados_fixed = open('mensagens_corrigidas.txt', 'w')

for msg in range(N):
    dados_fixed.write(' '.join(msgs_corrigidas[msg]) + '\n')

dados_fixed.close()
