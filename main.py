"""Punto de entrada: conecta el módulo UI con el módulo API."""
from api.consulta_covid import consultar_casos
from ui import interfaz


def main():
    interfaz.mostrar_bienvenida()
    while True:
        departamento = interfaz.pedir_departamento()
        limite = interfaz.pedir_limite()
        print("\nConsultando, espere un momento...")
        try:
            df = consultar_casos(departamento, limite)
            interfaz.mostrar_resultados(df)
        except Exception as error:  # sin internet, API caída, etc.
            interfaz.mostrar_error(error)
        if not interfaz.preguntar_continuar():
            print("\nHasta luego.")
            break


if __name__ == "__main__":
    main()
