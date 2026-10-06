"""Módulo API.

Única responsabilidad: comunicarse con el portal de Datos Abiertos
(datos.gov.co) y devolver los datos ya listos para mostrar.
No imprime nada ni pide datos al usuario (eso es del módulo ui).
"""
import unicodedata

import pandas as pd
from sodapy import Socrata

DOMINIO = "www.datos.gov.co"
ID_DATASET = "gt2j-8ykr"  # Casos positivos de COVID-19 en Colombia

# Nombre de la columna en el dataset -> título que se muestra al usuario
COLUMNAS = {
    "ciudad_municipio_nom": "Ciudad",
    "departamento_nom": "Departamento",
    "edad": "Edad",
    "fuente_tipo_contagio": "Tipo",
    "estado": "Estado",
    "pais_viajo_1_nom": "País de procedencia",
}


def normalizar_departamento(nombre):
    """El dataset guarda los nombres en MAYÚSCULAS y sin tildes."""
    sin_tildes = "".join(
        c for c in unicodedata.normalize("NFD", nombre)
        if unicodedata.category(c) != "Mn"
    )
    return sin_tildes.strip().upper()


def consultar_casos(nombre_departamento, limite_registros):
    """Consulta la API y devuelve un DataFrame con solo las columnas pedidas.

    Parámetros:
        nombre_departamento (str): departamento a consultar.
        limite_registros (int): número máximo de registros a traer.
    """
    departamento = normalizar_departamento(nombre_departamento)

    client = Socrata(DOMINIO, None, timeout=60)
    try:
        resultados = client.get(
            ID_DATASET,
            limit=limite_registros,
            departamento_nom=departamento,
        )
    finally:
        client.close()

    df = pd.DataFrame.from_records(resultados)
    if df.empty:
        return df

    # Si alguna columna no viene en un registro, se rellena con "N/A"
    df = df.reindex(columns=list(COLUMNAS.keys())).fillna("N/A")
    return df.rename(columns=COLUMNAS)
