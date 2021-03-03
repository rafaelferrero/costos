# Author: Rafael E. Ferrero


# BASE_PATH = "\\\srv-plm\InnovAx-PLM\\0.TCX-Docs\\70.CostoEstandar\\"
INPUT_PATH = "C:\\Users\\ferreror\\Desktop\\"
OUTPUT_PATH = "C:\\Users\\ferreror\\Desktop\\"

OUTPUT_WA = OUTPUT_PATH + "costo-workareas.csv"
OUTPUT_ITEMS = OUTPUT_PATH + "costo-piezas.csv"

MAESTRO_COMERCIALES = INPUT_PATH + "MaestroComerciales.xlsx"
MAESTRO_MP = INPUT_PATH + "MaestroMP.xlsx"
MAESTRO_COMPRAS = INPUT_PATH + "MaestroP_Compra.xlsx"
MAESTRO_WA = INPUT_PATH + "COSTO WA.xlsx"

piezas = {
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

workareas = {
    "work_areas": {
        "nombre_archivo": MAESTRO_WA,
        "nombre_hoja": "Salida",
        "columnas": {
            "codigo": 0,
            "costo": 3,
            }
        },
    }
