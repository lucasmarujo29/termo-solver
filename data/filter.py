# este arquivo será responsável por filtrar as palavras do dicionário, ou seja, pegar somente as palavras que sejam válidas para o jogo
# para isso, usarei alguns arquivos bases, que peguei do github do criador do jogo
# arquivo lexico: Léxico completo de palavras portuguesas de múltiplas fontes dicionárias (145.744 entradas)
# arquivo conjugações: Todas as conjugações verbais (195.751 formas)
# vou filtrar os dois

import unidecode


def removeRepeatingLines():
    dict_final = open("data/words-5-letters.txt", "w", encoding="utf-8")
    aux = open("data/aux.txt", "w", encoding="utf-8")

    wordsFinal=set()

    aux.close()
    dict_final.close()

def createMainList():
    b1 = open("data/lexico.txt", "r", encoding="utf-8") 
    b2 = open("data/conjugações.txt", "r", encoding="utf-8")
    aux = open("data/aux.txt", "w", encoding="utf-8")
    for line in b1:
        line = line.strip()
        #remover maiusculas
        line = line.lower()
        #remover acentos
        if(line != unidecode.unidecode(line)):
            line = unidecode.unidecode(line)
        #adicionar ao dicionario apenas se tiver 5 letras
        if len(line) == 5:
            aux.write(line + "\n")

    for line in b2:
        line = line.strip()
        #remover maiusculas
        line = line.lower()
        #remover acentos
        if(line != unidecode.unidecode(line)):
            line = unidecode.unidecode(line)
        #adicionar ao dicionario apenas se tiver 5 letras
        if (len(line) == 5) & (line.isalpha):
            aux.write(line + "\n")

    b1.close()
    b2.close()
    aux.close()

def main():
    
    createMainList()
    removeRepeatingLines()


if __name__ == "__main__":
    main()
