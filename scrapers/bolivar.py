import requests


URL_BOLIVAR = (
    "https://www.segurosbolivar.com/arcgis/rest/services/"
    "ARL/seleccionProovedorARL/GPServer/"
    "seleccionProovedor/execute"
)


def consultar_bolivar(
    ciudad="PASTO",
    departamento="NARIÑO",
    servicio="FARMACIA",
    direccion=""
):
    parametros = {
        "direccion": direccion,
        "ciudad": ciudad,
        "departamento": departamento,
        "longitud": "",
        "latitud": "",
        "servicio": servicio,
        "especialidad": "",
        "subespecialidad": "",
        "f": "json",
    }

    respuesta = requests.get(
        URL_BOLIVAR,
        params=parametros,
        timeout=30
    )

    print("URL consultada:")
    print(respuesta.url)

    print("Código HTTP:")
    print(respuesta.status_code)

    print("Respuesta cruda:")
    print(respuesta.text)

    respuesta.raise_for_status()

    return respuesta.json()


if __name__ == "__main__":
    datos = consultar_bolivar()

    print("Respuesta Seguros Bolívar:")
    print(datos)
