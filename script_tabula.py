from tabula import convert_into_by_batch 

# pdf = read_pdf("notas_clear", batch="notas_clear/", area=(237.628,33.841,445.134,558.184))
pdfs = convert_into_by_batch("notas_clear/", output_format="csv")
print(pdfs)