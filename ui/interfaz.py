"""Módulo UI.

Única responsabilidad: hablar con el usuario (pedir datos y mostrar
resultados). No sabe nada de la API.
"""

LIMITE_MAXIMO = 1000  # un número muy grande puede "colgar" la consulta

# Ancho de cada columna al imprimir la tabla
FORMATO_FILA = "{:<22} {:<16} {:<6} {:<14} {:<14} {:<20}"


def mostrar_bienvenida():
    print("=" * 60)
    print("  CONSULTA DE CASOS COVID-19 EN COLOMBIA (datos.gov.co)")
    print("=" * 60)


def pedir_departamento():
    while True:
        nombre = input("\nDepartamento a consultar (ej. Risaralda): ").strip()
        if nombre:
            return nombre
        print("  El departamento no puede estar vacío.")


def pedir_limite():
    while True:
        texto = input(f"Número de registros (1 a {LIMITE_MAXIMO}): ").strip()
        if texto.isdigit() and 1 <= int(texto) <= LIMITE_MAXIMO:
            return int(texto)
        print(f"  Ingrese un número entero entre 1 y {LIMITE_MAXIMO}.")


def mostrar_resultados(df):
    """Imprime el DataFrame usando str.format con columnas alineadas."""
    if df.empty:
        print("\nNo se encontraron registros para ese departamento.")
        print("Tip: escríbalo como en el dataset (ej. 'Valle', 'Bogota D.C.').")
        return

    encabezado = FORMATO_FILA.format(*df.columns)
    print("\n" + encabezado)
    print("-" * len(encabezado))
    for fila in df.itertuples(index=False):
        print(FORMATO_FILA.format(*[str(v)[:22] for v in fila]))
    print(f"\nTotal de registros mostrados: {len(df)}")


def mostrar_error(mensaje):
    print(f"\n[ERROR] No se pudo completar la consulta: {mensaje}")


def preguntar_continuar():
    return input("\n¿Hacer otra consulta? (s/n): ").strip().lower() == "s"
