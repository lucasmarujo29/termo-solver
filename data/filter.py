# este arquivo será responsável por filtrar as palavras do dicionário, ou seja, pegar somente as palavras que sejam válidas para o jogo
# o dicionário que peguei do Libre Office possui a seguinte formatação:
# o primeiro elemento é o número de palavras, depois tem cada palavra, algumas com um "palavra/categoria"
# ou seja preciso:
# 
# 1. remover as categorias, ou seja, tudo que vier depois de uma barra (/) em cada palavra
# 2. remover letras maiusculas, caracteres especiais, sendo acentos, hífens e etc
# 3. remover palavras que não tenham exatamente 5 letras
#

dict_base = open("dicitonary.txt", "r")
dict_final = open("dictionary_modified.txt", "w")


for line in dict_base:
    line01 = line.strip()
    
    #remover tag
        
    #remover maiusculas
    if line01.isupper():
        line01 = line01.lower()

dict_base.close()
dict_final.close()