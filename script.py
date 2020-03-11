from pdfminer import high_level
from os import listdir 

lista_pdfs = list(filter(lambda x: x.endswith('.pdf'), listdir('notas_clear/')))
lista_pdfs = list(map(lambda x: 'notas_clear/' + x, lista_pdfs))

for pdf in lista_pdfs:
	print(high_level.extract_text(pdf))
