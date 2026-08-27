from supabase_client import supabase


def probar_conexion():
    respuesta = supabase.table("arl").select("*").execute()

    print("ARL registradas:")

    for arl in respuesta.data:
        print(f"- {arl['nombre']}")


if __name__ == "__main__":
    probar_conexion()
