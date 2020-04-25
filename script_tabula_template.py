from os import listdir
from tabula import read_pdf, read_pdf_with_template
import pandas as pd

lista_pdfs = list(filter(lambda x: x.endswith('.pdf'), listdir('notas_clear/')))
lista_pdfs = list(map(lambda x: 'notas_clear/' + x, lista_pdfs))

initial_dataframe = read_pdf_with_template(lista_pdfs[0], "NotaNegociacao.tabula-template.json")[0]

#initial_dataframe = []

for pdf in lista_pdfs:
    data_arquivo = pdf.rsplit("_", -1)[-1].rsplit(".", -1)[0]
    print(data_arquivo)
#    initial_dataframe['data'] = data_arquivo
    initial_dataframe = initial_dataframe.append(read_pdf_with_template(pdf, "NotaNegociacao.tabula-template.json")[0])

print(initial_dataframe)
