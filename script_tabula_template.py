from os import listdir
from tabula import read_pdf
import pandas as pd

lista_pdfs = list(filter(lambda x: x.endswith('.pdf'), listdir('notas_clear/')))
lista_pdfs = list(map(lambda x: 'notas_clear/' + x, lista_pdfs))

initial_dataframe = read_pdf(lista_pdfs[0], output_format="dataframe", stream=True, area=(237.628,33.841,445.134,558.184))[0]

for pdf in lista_pdfs:
    data_arquivo = pdf.rsplit("_", -1)[-1].rsplit(".", -1)[0]
    print(data_arquivo)
    initial_dataframe['data'] = data_arquivo
    initial_dataframe = initial_dataframe.append(read_pdf(pdf, "NotaNegociacao.tabula-template.json")), ignore_index=True)

print(initial_dataframe)
