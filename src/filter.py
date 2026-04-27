# este arquivo será responsável por filtrar as palavras do dicionário, ou seja, pegar somente as palavras que sejam válidas para o jogo
# para isso, usarei alguns arquivos bases, que peguei do github do criador do jogo
# arquivo lexico: Léxico completo de palavras portuguesas de múltiplas fontes dicionárias (145.744 entradas)
# arquivo conjugações: Todas as conjugações verbais (195.751 formas)
# vou filtrar os dois
# rodar esse arquivo cria o dicionario de cinco letras

import unidecode


def removeRepeatingLines(): #falta implementar
    dict_final = open("data/words-5-letters.txt", "w", encoding="utf-8")
    aux = open("data/aux.txt", "w", encoding="utf-8")
    # duas opções para remover as linhas repetidas:
    # 1. ler o arquivo e só adicionar uma linha em outro arquivo caso a linha anterior ou a linha sucessiva seja diferente
    # 2. ler o arquivo e fazer um set (estrutura de dado que não aceita elementos repetidos) e depois escrever o set inteiro em outro arquivo
    wordsFinal=set()

    aux.close()
    dict_final.close()

def createMainList():
    b1 = open("data/lexico.txt", "r", encoding="utf-8") #abre o arquivo lexico para leitura
    b2 = open("data/conjugações.txt", "r", encoding="utf-8") #abre o arquivo conjugações para leitura
    aux = open("data/aux.txt", "w", encoding="utf-8") #abre o arquivo aux.txt para escrita, onde serão escritas as palavras filtradas
    for line in b1: #for que percorre as linhas do arquivo
        line = line.strip() #a função strip() remove os espaços em branco no inicio e final da string (que no caso é a linha do arquivo)
        line = line.lower() #a função lower() transforma todas as letras da string em minúsculas
        if(line != unidecode.unidecode(line)):
            line = unidecode.unidecode(line)
        #esse último trecho usa uma biblioteca com uma função para remover acentos
        #como só adicionaremos palavras de 5 letras, usamos a função len() para verificar
        if len(line) == 5:
            aux.write(line + "\n")
    for line in b2: #REPETIÇÃO DO MESMO PROCESSO PARA O OUTRO ARQUIVO
        line = line.strip()
        line = line.lower()
        if(line != unidecode.unidecode(line)):
            line = unidecode.unidecode(line)
        if (len(line) == 5) & (line.isalpha): #a função isalpha() verifica se a string é composta somente por letras, ou seja, não tem números ou caracteres especiais
            aux.write(line + "\n")

    b1.close()
    b2.close()
    aux.close()

def main():
    
    createMainList()
    removeRepeatingLines()


if __name__ == "__main__":
    main()
