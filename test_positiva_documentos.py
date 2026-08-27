from scrapers.positiva_documentos import buscar_pasto


resultados = buscar_pasto()

print("TOTAL:", len(resultados))

for resultado in resultados:
    print("\n-------------------------")
    print("Página:", resultado["pagina"])
    print(resultado["texto"])
