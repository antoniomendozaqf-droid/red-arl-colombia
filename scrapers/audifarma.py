import requests
from bs4 import BeautifulSoup


URL_AUDIFARMA = (
    "https://encasa.audifarma.com.co/"
    "formularioSeguimiento/faces/cafs.xhtml"
)


def inspeccionar_audifarma():
    sesion = requests.Session()

    headers = {
        "User-Agent": (
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
            "AppleWebKit/537.36 (KHTML, like Gecko) "
            "Chrome/120.0 Safari/537.36"
        ),
        "Accept": (
            "text/html,application/xhtml+xml,"
            "application/xml;q=0.9,*/*;q=0.8"
        ),
        "Accept-Language": "es-CO,es;q=0.9",
    }

    try:
        respuesta = sesion.get(
            URL_AUDIFARMA,
            headers=headers,
            timeout=60
        )

        print("URL FINAL:", respuesta.url)
        print("HTTP:", respuesta.status_code)
        print("CONTENT-TYPE:", respuesta.headers.get("content-type"))

        print("\nPRIMEROS 1000 CARACTERES:")
        print(respuesta.text[:1000])

        if respuesta.status_code != 200:
            return

        soup = BeautifulSoup(respuesta.text, "html.parser")

        print("\nFORMULARIOS:")
        for form in soup.find_all("form"):
            print(
                "id=", form.get("id"),
                "action=", form.get("action"),
                "method=", form.get("method")
            )

        print("\nSELECTORES:")

        for select in soup.find_all("select"):
            print(
                "\nSELECT:",
                "name=", select.get("name"),
                "id=", select.get("id")
            )

            for option in select.find_all("option")[:50]:
                print(
                    "   ",
                    option.get_text(" ", strip=True),
                    "=>",
                    option.get("value")
                )

        print("\nINPUTS:")

        for entrada in soup.find_all("input"):
            print(
                "type=", entrada.get("type"),
                "name=", entrada.get("name"),
                "id=", entrada.get("id"),
                "value=", entrada.get("value")
            )

        print("\nSCRIPTS:")

        for script in soup.find_all("script", src=True):
            print(script.get("src"))

    except Exception as error:
        print("ERROR AL CONSULTAR AUDIFARMA:")
        print(type(error).__name__)
        print(str(error))


if __name__ == "__main__":
    inspeccionar_audifarma()
