# ProyectoAPI – Casos positivos de COVID-19 en Colombia

Proyecto de Fundamentos Básicos de Python (UTP). Consulta el dataset
**Casos positivos de COVID-19 en Colombia** (`gt2j-8ykr`) del portal
datos.gov.co y muestra: Ciudad, Departamento, Edad, Tipo, Estado y
País de procedencia.

## Estructura
```
ProyectoAPI/
├── api/
│   ├── __init__.py
│   └── consulta_covid.py   # consulta a la API (sodapy + pandas)
├── ui/
│   ├── __init__.py
│   └── interfaz.py         # entrada/salida por consola
├── main.py                 # punto de entrada
├── requirements.txt
└── README.md
```

## Cómo ejecutarlo
```bash
python -m venv venv
venv\Scripts\activate          # Windows  (Mac/Linux: source venv/bin/activate)
pip install -r requirements.txt
python main.py
```

## Notas
- Los departamentos en el dataset están en mayúsculas y sin tildes
  (ej. `VALLE`, `BOGOTA D.C.`, `RISARALDA`); el programa ya normaliza lo que escribas.
- Límite máximo de registros: 1000 (más puede "colgar" la consulta).
