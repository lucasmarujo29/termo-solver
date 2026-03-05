# este arquivo será responsável por filtrar as palavras do dicionário, ou seja, pegar somente as palavras que sejam válidas para o jogo
# o dicionário que peguei do Libre Office possui a seguinte formatação:
# o primeiro elemento é o número de palavras, depois tem cada palavra, algumas com um "palavra/categoria"
# ou seja preciso:
# 
# 1. remover as categorias, ou seja, tudo que vier depois de uma barra (/) em cada palavra
# 2. remover letras maiusculas, caracteres especiais, sendo acentos, hífens e etc
# 3. remover palavras que não tenham exatamente 5 letras
#
import unidecode

dict_base = open("dicitonary.txt", "r")
dict_final = open("dictionary_modified.txt", "w")


for line in dict_base:
    line = line.strip()
    #remover tag
    posSlash = line.find("/")
    if(posSlash != -1):
        line = line[0:posSlash]
    #remover maiusculas
    if line.isupper():
        line = line.lower()
    #remover acentos
    if(line != unidecode(line)):
        line = unidecode(line)
    #adicionar ao dicionario apenas se tiver 5 letras
    if len(line) == 5:
        dict_final(line,"w")

dict_base.close()
dict_final.close()