import re
import PyPDF2


###############################################
# Print an f-string that displays NLP stands for Natural Language Processing using the variables provided
abbr = 'NLP'
full_text = 'Natural Language Processing'

print(f'{abbr} stands for {full_text}')

###############################################
# Create a file in the current working directory called contacts.txt
with open('contacts.txt', 'w') as c:
    c.write('First_Name Last_Name, Title, Extension, Email')

with open('contacts.txt') as c:
    fields = c.read()

print(fields)

###############################################
# Use PyPDF2 to open the file Business_Proposal.pdf. Extract the text of page 2
f = open('Business_Proposal.pdf', 'rb')
pdf_reader = PyPDF2.PdfFileReader(f)

# pegando uma pag
page = pdf_reader.getPage(1)

# extraindo o txt
page_text = page.extractText()

# lendo o txt
print(page_text)

# fechando
f.close()

###############################################
# Open the file contacts.txt in append mode. Add the text of page 2 from above to contacts.txt
with open('contacts.txt', 'a') as c:
    c.write(page_text)

with open('contacts.txt') as c:
    fields = c.read()

print('------------------------------------')
print(fields)

###############################################
# Regex
# Using the page_text variable created above, extract any email addresses that were contained in the
# file Business_Proposal.pdf

pattern = r'\S+@\S+'

print(re.findall(pattern, page_text))
