import requests
from bs4 import BeautifulSoup


URL_POSITIVA = "https://positiva.gov.co/"


def buscar_fuentes_positiva():
    respuesta = requests.get(
        URL_POSITIVA,
        timeout=30,
        headers={
            "User-Agent": "Mozilla/5.0 RedARLColombia/1.0"
        }
    )

    respuesta.raise_for_status()

    soup = BeautifulSoup(respuesta.text, "html.parser")

    enlaces = []

    for link in soup.find_all("a", href=True):
        href = link["href"]
        texto = link.get_text(" ", strip=True)

        combinado = f"{texto} {href}".lower()

        if any(
            palabra in combinado
            for palabra in [
                "medicamento",
                "farmacia",
                "dispensacion",
                "dispensación",
                "red asistencial",
            ]
        ):
            enlaces.append(
                {
                    "texto": texto,
                    "url": href
                }
            )

    return enlaces


if __name__ == "__main__":
    resultados = buscar_fuentes_positiva()

    print("Fuentes encontradas en Positiva:")

    for resultado in resultados:
        print(resultado)
