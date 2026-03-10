# termo-solver
"Termo" is a game where you need to guess in 6 attemps a 5 letter word, in portuguese. The ideia is creating a program that can solve any word of the day. Initially, it would solve only the "Termo", not the "Dueto", nor "Quarteto"
I'll be using python, so i can learn more doing this project

---------------------NOTES---------------------
1) Take a list of all the portuguese words
2) "Filter" those words to only acceptable words (exactly five letter, no acentuation, no names and etc) 
3) Analyse data to see wich letters are most common, syllabes maybe
4) Determine an strategy of solving Termos. 



On the paste "data", there are 3 bases to the 5 letter dicitonary, "conjugações" contains all verbs and their respective conjugation, "lexico" has all words on portuguese dictionary and icf is basic a rellation word-frequency on common dialect.
ICF (Inverse Corpus Frequency):
ICF é uma medida de raridade/importância da palavra calculada como o inverso da frequência com que uma palavra aparece em múltiplos corpora portugueses. Pontuações ICF mais baixas indicam palavras mais comuns (ex: "de" = 3,02), enquanto pontuações mais altas indicam termos mais raros e especializados. Isso substitui a abordagem anterior de TF (Term Frequency) e fornece melhor ponderação para análise de conteúdo e aplicações de processamento de linguagem.
