from datetime import datetime

name = 'Fred'

################################################################
# formato antigo
print('His name is {var}.'.format(var=name))
print('\n')

################################################################
# f-strings:
print(f'His name is {name}.')
print(f'His name is {name!r}')  # add aspas na var
print('\n')

################################################################
# f-strings com dict
d = {'a': 123, 'b': 456}
print(f"Address: {d['a']} Main Street")
print('\n')

################################################################
# f-strings com array
library = [('Author', 'Topic', 'Pages'),
           ('Twain', 'Rafting in river', 601),
           ('Feynman', 'Physics', 95),
           ('Hamilton', 'Mythology', 144)]

################################################################
# f-strings no for
for book in library:
    # com esse formato, a identação ficará toda desorganizada no print
    print(f'{book[0]} {book[1]} {book[2]}')
print('\n')

################################################################
for book in library:
    # com esse formato, a identação ficará organizada no print pois passamos
    # a qdade de char totais que tal var pode ocupar com param após o ':'
    print(f'{book[0]:{10}} {book[1]:{30}} {book[2]:{7}}')
print('\n')

################################################################
for book in library:
    # com esse formato, empurramos o último lugar para encostar na margem dir do print usando >
    print(f'{book[0]:{10}} {book[1]:{30}} {book[2]:>{7}}')
print('\n')

################################################################
for book in library:
    # com esse formato, empurramos o último lugar para encostar na margem dir do print usando >
    # E completamos os char em branco com '.', mas poderia ser qquer outro char
    print(f'{book[0]:{10}} {book[1]:{30}} {book[2]:.>{7}}')  # here .> was added
print('\n')

################################################################
# formatando datas
# para mais formatos de data: https://docs.python.org/3/reference/lexical_analysis.html#f-strings
today = datetime(year=2018, month=1, day=27)
print(f'{today:%B %d, %Y}')
print('\n')

# ###############################################################
# ###############################################################
# ###################### Manipulando arqvs ######################
# ###############################################################
# ###############################################################

#################################################################
# abrindo arqv txt
my_file = open('test.txt')

################################################################
# abrindo arqv
print(my_file.read())

# nota: se tentarmos ler novamente o arqv, n veremos nada pois o cursos do python
# estará no fim do doc, precisamos levá-lo novamente ao início
print('-------------------------')
print("lendo novamente: " + my_file.read())
print('-------------------------')

my_file.seek(0)
print("lendo após seek:\n" + my_file.read())
print('\n')

# se colocarmos o conteúdo em uma var, seek n é mais necessário
my_file.seek(0)
content = my_file.read()
print(content)
print('#############################')
print(content)
print('#############################')

################################################################
# lendo linha a linha

# com o cmd abaixo, fazemos um array em que cada linha é um elemento
my_file.seek(0)
print(my_file.readlines())
print('\n')

################################################################
# fechando o arqv
my_file.close()

################################################################
# escrevendo sobre um arqv

# abrindo novamente
# PS: abrir com 'w' ou 'w+' faz com que o conteúdo do arqv seja sobrescrito
my_file = open('test.txt', 'w+')

my_file.write('This is a new first line')

my_file.seek(0)
print(my_file.read())
print('\n')

my_file.close()

################################################################
# add ao fim de um arv (append)

# 'a' permite fazer uma add ao final do arqv
my_file = open('test.txt', 'a+')
my_file.write('\nThis line is being appended to test.txt')
my_file.write('\nAnd another line here.')

my_file.seek(0)
print(my_file.read())

my_file.close()


# ###############################################################
# ###############################################################
# ################### Trabalhando com contexto ##################
# ###############################################################
# ###############################################################

# para que não haja erro de não fechar o arqv, podemos usar contexto
# ele se encarregará de fechar o arqv assim as operação terminarem
with open('test.txt', 'r') as txt:
    first_line = txt.readlines()[0]

print(first_line)

################################################################
# iterando em um arqv
with open('test.txt', 'r') as txt:
    for line in txt:
        print(line, end='')
