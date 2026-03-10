# # este arquivo será responsável por filtrar as palavras do dicionário, ou seja, pegar somente as palavras que sejam válidas para o jogo
# # o dicionário que peguei do Libre Office possui a seguinte formatação:
# # o primeiro elemento é o número de palavras, depois tem cada palavra, algumas com um "palavra/categoria"
# # ou seja preciso:
# # 
# # 1. remover as categorias, ou seja, tudo que vier depois de uma barra (/) em cada palavra
# # 2. remover letras maiusculas, caracteres especiais, sendo acentos, hífens e etc
# # 3. remover palavras que não tenham exatamente 5 letras
# #
# import unidecode
# import os

# print(os.getcwd())

# dict_base = open("data/dictionary.txt", "r", encoding="utf-8")
# dict_final = open("data/dictionary_modified.txt", "w", encoding="utf-8")


# for line in dict_base:
#     line = line.strip()
#     #remover tag
#     posSlash = line.find("/")
#     if(posSlash != -1):
#         line = line[0:posSlash]
#     #remover maiusculas
#     line = line.lower()
#     #remover acentos
#     if(line != unidecode.unidecode(line)):
#         line = unidecode.unidecode(line)
#     #adicionar ao dicionario apenas se tiver 5 letras
#     if len(line) == 5:
#         dict_final.write(line + "\n")

# dict_base.close()
# dict_final.close()

