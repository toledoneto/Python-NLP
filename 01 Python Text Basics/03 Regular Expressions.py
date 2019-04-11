# expressões regulares (regex) nos ajudam a encontrar um específico padrão dentro de um texto, p.e:
# * data
# * num de telefone
# * qquer coisa que tenha um formato conhecido
# documentação: https://docs.python.org/3/library/re.html
#               https://docs.python.org/3/howto/regex.html

import re  # importa a lib de regex


# vamos usar essa string para buscar algumas palavras
text = "The agent's phone number is 408-555-1234. Call soon!"

##################################################################
# buscas com 'in'

print('phone' in text)  # true

##################################################################
# usando re

pattern = 'phone'
# span => char de início, fim de onde foi encontrado o
# match => caso encontrado
print(re.search(pattern, text))  # <_sre.SRE_Match object; span=(12, 17), match='phone'>

pattern = "NOT IN TEXT"
print(re.search(pattern, text))  # None

##################################################################
# mais de match

pattern = 'phone'

match = re.search(pattern, text)

print(match)  # <_sre.SRE_Match object; span=(12, 17), match='phone'>

# local onde foi achado
print(match.span())  # (12, 17)

# início
match.start()  # 12

# fim
match.end()  # 17

# mais de um ocorrência do msm padrão
text = "my phone is a new phone"

match = re.search("phone", text)

# ele vai encontar apenas o primeiro ocorrido
print(match.span())  # (3, 8)

# para achar TODAS ocorrências
matches = re.findall("phone", text)

print(matches)  # ['phone', 'phone']
print(len(matches))  # 2

# buscando cada obj isoladamente
for match in re.finditer("phone", text):
    print(match.span())  # (3, 8)
                         # (18, 23)

# se quiser o texto exato a ser procurado
print(match.group())  # 'phone'

# ###############################################################
# ###############################################################
# ########## Procurando padrões de valor não conhecidos #########
# ###############################################################
# ###############################################################

# o uso de '\' indica ao python que n procuramos aquele char em específico
# mas sim que estamos passando um símbolo que tem um significado no regex

# alguns símbolos de regex que podem ser usados
# char      desc               exp padrão   exp match
# * \d  	A digit	           file_\d\d	file_25
# * \w  	Alphanumeric       \w-\w\w\w	A-b_1
# * \s  	White space	       a\sb\sc	    a b c
# * \D  	A non digit	       \D\D\D	    ABC
# * \W  	Non-alphanumeric   \W\W\W\W\W	*-+=)
# * \S  	Non-whitespace	   \S\S\S\S	    Yoyo

# frase
text = "My telephone number is 408-555-1234"

# regex de um num telefone com 3 dig, um -, 3 dig, um - e, por fim, 4 dig
phone = re.search(r'\d\d\d-\d\d\d-\d\d\d\d', text)

print(phone.group())

# a quantidade de \d pode começar a ficar grande, para lidar com isso, usamos....

##################################################################
# Quantifiers

# char	         desc	                    exp padrão	         exp match
# +	             Occurs one or more times	Version \w-\w+	     Version A-b1_1
# {3}	         Occurs exactly 3 times	    \D{3}	             abc
# {2,4}	         Occurs 2 to 4 times	    \d{2,4}	             123
# {3,}	         Occurs 3 or more	        \w{3,}	             anycharacters
# \*	         Occurs zero or more times	A\*B\*C*	         AAACC
# ?	             Once or none	            plurals?	         plural

# refazendo a busca do num telefone com quantifiers
# <_sre.SRE_Match object; span=(23, 35), match='408-555-1234'>
print(re.search(r'\d{3}-\d{3}-\d{4}', text))

##################################################################
# Grupos

# podemos usar () para separar em grupos um cnj de regex encontrado, por explo
phone_pattern = re.compile(r'(\d{3})-(\d{3})-(\d{4})')  # temos 3 gpos entre ()

results = re.search(phone_pattern, text)

print(results.group())  # '408-555-1234'
print(results.group(1))  # 408
print(results.group(2))  # 555
print(results.group(3))  # 1234

##################################################################
# Mais operadores de regex

# ...................
# OR usando |
print(re.search(r"man|woman", "This man was here."))  # <_sre.SRE_Match object; span=(5, 8), match='man'>
print(re.search(r"man|woman", "This woman was here."))  # <_sre.SRE_Match object; span=(5, 10), match='woman'>

# ...................
# 'Wildcard': usando '.' podemos dizer 'qquer coisa naquele lugar vale'
print(re.findall(r".at", "The cat in the hat sat here."))  # ['cat', 'hat', 'sat']

# apenas com '.', não pegamos tds as palavras
print(re.findall(r".at", "The bat went splat"))  # ['bat', 'lat']

# com quantifiers, pegamos mais que o desejado
print(re.findall(r"...at", "The bat went splat"))  # ['e bat', 'splat']

# se quisermos pegar apenas as palavras
print(re.findall(r'\S+at', "The bat went splat"))  # ['bat', 'splat']

# ...................
# Começa e Termina com
# termina com num
print(re.findall(r'\d$', 'This ends with a number 2'))  # ['2']

# começa com num
print(re.findall(r'^\d', '1 is the loneliest number.'))

# ...................
# excluindo char
# para excluir char, usamos o conj ^ com [], tudo dentro de [^] será excluído
phrase = "there are 3 numbers 34 inside 5 this sentence."
print(re.findall(r'[^\d]', phrase))  # vai ficar um vetor de cada letra

# para obter as palavras novamente, usamos o sinal de '+'.
# Elas virão na forma de vetor
print(re.findall(r'[^\d]+', phrase))  # ['there are ', ' numbers ', ' inside ', ' this sentence.']

# o processo acima é útil para excluir pontuações de uma frase
test_phrase = 'This is a string! But it has punctuation. How can we remove it?'
print(re.findall('[^!.? ]+', test_phrase))

# vamos tirar da forma de vetor e votar para string
clean = ' '.join(re.findall('[^!.? ]+', test_phrase))
print(clean)  # 'This is a string But it has punctuation How can we remove it'

# ...................
# agrupando
# podemos usar [] para agrupar. No caso abaixo, apenas as palavras com hífen
text = 'Only find the hypen-words in this sentence. But you do not know how long-ish they are'
print(re.findall(r'[\w]+-[\w]+', text))  # ['hypen-words', 'long-ish']

# ...................
# () para múltiplas opçs
# achar palavras que:
# * começam com 'cat'
# * E terminam uma dessas -> 'fish','nap', or 'claw'
text = 'Hello, would you like some catfish?'
texttwo = "Hello, would you like to take a catnap?"
textthree = "Hello, have you seen this caterpillar?"

print(re.search(r'cat(fish|nap|claw)', text))  # <_sre.SRE_Match object; span=(27, 34), match='catfish'>

print(re.search(r'cat(fish|nap|claw)', texttwo))  # <_sre.SRE_Match object; span=(32, 38), match='catnap'>

print(re.search(r'cat(fish|nap|claw)', textthree))  # None

