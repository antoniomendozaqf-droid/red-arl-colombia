from scrapers.positiva import buscar_fuentes_positiva


resultados = buscar_fuentes_positiva()

print("TOTAL:", len(resultados))

for resultado in resultados:
    print(resultado)
