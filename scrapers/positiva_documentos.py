import requests
import io
from pypdf import PdfReader


DOCUMENTOS = [
    "https://portalvida.positiva.gov.co/documents/2978451/3179262/Habilitaci%C3%B3n%2BT%C3%A9cnica.pdf/d021c17c-15d4-52dc-fd4c-b5ed836f8e38?download=true&t=1701230637396",
    "https://www.positiva.gov.co/documents/2978451/3451029/Anexo_No._9_Ficha_Tecnica.pdf/377970fc-b89b-8745-3f61-4b048f32e290?download=true&t=1702400326868"
]


def buscar_pasto():
    resultados = []

    for url in DOCUMENTOS:
        print("\nConsultando:")
        print(url)

        respuesta = requests.get(
            url,
            timeout=60,
            headers={"User-Agent": "Mozilla/5.0"}
        )

        print("HTTP:", respuesta.status_code)

        if respuesta.status_code != 200:
            continue

        lector = PdfReader(io.BytesIO(respuesta.content))

        for numero, pagina in enumerate(lector.pages, start=1):
            texto = pagina.extract_text() or ""

            texto_lower = texto.lower()

            if (
                "pasto" in texto_lower
                or "nariño" in texto_lower
                or "dispensacion" in texto_lower
                or "dispensación" in texto_lower
            ):
                resultados.append({
                    "url": url,
                    "pagina": numero,
                    "texto": texto[:3000]
                })

    return resultados


if __name__ == "__main__":
    resultados = buscar_pasto()

    print("\nTOTAL RESULTADOS:", len(resultados))

    for resultado in resultados:
        print("\n==========================")
        print("PÁGINA:", resultado["pagina"])
        print(resultado["texto"])
