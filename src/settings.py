# Author: Rafael E. Ferrero


# BASE_PATH = "\\\srv-plm\InnovAx-PLM\\0.TCX-Docs\\70.CostoEstandar\\"
BASE_PATH = "C:\\Users\\ferreror\\Desktop\\"

MAESTRO_COMERCIALES = BASE_PATH + "MaestroComerciales.xlsx"
MAESTRO_MP = BASE_PATH + "MaestroMP.xlsx"
MAESTRO_COMPRAS = BASE_PATH + "MaestroP_Compra.xlsx"
MAESTRO_WA = BASE_PATH + "COSTO WA.xlsx"

archivos = {
    "comerciales": {
        "nombre_archivo": MAESTRO_COMERCIALES,
        "nombre_hoja": "Sheet1",
        "columnas": {
            "codigo": 0,
            "costo": 14,
            }
        },
    "materias_primas": {
        "nombre_archivo": MAESTRO_MP,
        "nombre_hoja": "Sheet1",
        "columnas": {
            "codigo": 0,
            "costo": 19,
            }
        },
    "compras": {
        "nombre_archivo": MAESTRO_COMPRAS,
        "nombre_hoja": "Sheet1",
        "columnas": {
            "codigo": 1,
            "costo": 10,
            }
        },
    }
"""
    "work_areas": {
        "nombre_archivo": MAESTRO_WA,
        "nombre_hoja": "Salida",
        "columnas": {
            "codigo": 1,
            "costo": 4,
            }
        },
"""
OUTPUT_FILE = BASE_PATH + "ParaNetsuite.csv"
