import requests
from bs4 import BeautifulSoup


URL_AUDIFARMA = "https://www.audifarma.com.co/inicio/red-de-farmacias"


def inspeccionar_audifarma():
    respuesta = requests.get(
        URL_AUDIFARMA,
        timeout=30,
        headers={
            "User-Agent": "Mozilla/5.0 RedARLColombia/1.0"
        }
    )

    print("HTTP:", respuesta.status_code)

    respuesta.raise_for_status()

    soup = BeautifulSoup(respuesta.text, "html.parser")

    print("\nFORMULARIOS:")
    for form in soup.find_all("form"):
        print("ACTION:", form.get("action"))
        print("METHOD:", form.get("method"))

    print("\nSELECTORES:")
    for select in soup.find_all("select"):
        print(
            "name=", select.get("name"),
            "id=", select.get("id")
        )

        opciones = []

        for option in select.find_all("option"):
            opciones.append(
                {
                    "texto": option.get_text(" ", strip=True),
                    "value": option.get("value")
                }
            )

        print(opciones[:30])

    print("\nSCRIPTS RELEVANTES:")

    for script in soup.find_all("script", src=True):
        src = script.get("src")

        if any(
            palabra in src.lower()
            for palabra in [
                "farm",
                "red",
                "search",
                "consulta",
                "api"
            ]
        ):
            print(src)


if __name__ == "__main__":
    inspeccionar_audifarma()
