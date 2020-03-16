from os import listdir
from tabula import read_pdf 

lista_pdfs = list(filter(lambda x: x.endswith('.pdf'), listdir('notas_clear/')))
lista_pdfs = list(map(lambda x: 'notas_clear/' + x, lista_pdfs))

notas_clear = []

for pdf in lista_pdfs:	
	notas_clear.append(read_pdf(pdf, area=(237.628,33.841,445.134,558.184)))	

# pdfs = convert_into_by_batch("notas_clear/", output_format="csv")




