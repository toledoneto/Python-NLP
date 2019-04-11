# NOTA: nem td PDF poderá ser lido através desse método, em especial aqueles vindos de imgs de escaner

import PyPDF2


# 'rb' significa 'reading binary', o necessário para ler PDF
f = open('US_Declaration.pdf', 'rb')

# lendo
pdf_reader = PyPDF2.PdfFileReader(f)

# num pag
print(pdf_reader.numPages)

# pegando uma pag
page_one = pdf_reader.getPage(0)

# extraindo o txt
page_one_text = page_one.extractText()

# lendo o txt
print(page_one_text)

# fechando
f.close()

# ###############################################################
# ###############################################################
# ################## Adicionando linhas no PDF ##################
# ###############################################################
# ###############################################################

# não podemos incluir diretamente no PDF, porém podemos fazer uma cópia da pag
# e add ao fim do arqv
f = open('US_Declaration.pdf', 'rb')
pdf_reader = PyPDF2.PdfFileReader(f)

first_page = pdf_reader.getPage(0)

# criando o escritor
pdf_writer = PyPDF2.PdfFileWriter()

pdf_writer.addPage(first_page)

pdf_output = open("Some_New_Doc.pdf", "wb")

pdf_writer.write(pdf_output)

pdf_output.close()
f.close()

# ###############################################################
# ###############################################################
# ######################### Outro explo #########################
# ###############################################################
# ###############################################################

f = open('US_Declaration.pdf', 'rb')

# listando tds as pgs
# o índice será correspondente ao num de pág
pdf_text = [0]  # zero foi incluido para fazer a pag 1 ter índice 1

pdf_reader = PyPDF2.PdfFileReader(f)

for p in range(pdf_reader.numPages):
    page = pdf_reader.getPage(p)

    pdf_text.append(page.extractText())

f.close()

print(pdf_text)

print(pdf_text[2])
