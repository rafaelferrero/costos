# Author: Rafael E. Ferrero

"""
    This program receive an Excel file and extract specific data into .csv file
"""


import os
import pyexcel as pe  # http://docs.pyexcel.org/
from datetime import datetime as dt
from hashbang import command
from settings import (
    OUTPUT_WA,
    OUTPUT_ITEMS,
    piezas,
    workareas,
    )


@command
def main():
    # Proceso de archivo de costos de Work Areas
    wabook = pe.get_book(
        file_name=workareas["work_areas"]["nombre_archivo"],
        sheets=[workareas["work_areas"]["nombre_hoja"],]
    )
    csvwa = []
    for r in range(1, len(wabook[workareas["work_areas"]["nombre_hoja"]])):
        temp = {}
        for c in workareas["work_areas"]["columnas"].keys():
            if c=="codigo":
                temp.update({
                    c: wabook[
                        workareas["work_areas"]["nombre_hoja"]][
                            r, workareas["work_areas"]["columnas"][c]][11:-6]
                })
            else:
                temp.update({
                    c: wabook[
                        workareas["work_areas"]["nombre_hoja"]][
                            r, workareas["work_areas"]["columnas"][c]]
                })
        csvwa.append(temp)
        
    if os.path.exists(OUTPUT_WA):
        try:
            os.remove(OUTPUT_WA)
        except:
            pass
    output_file = pe.get_sheet(records=csvwa)
    output_file.save_as(OUTPUT_WA)

    # Proceso de archivo de costos de materiales e items comerciales
    csvpiezas = []
    for k in piezas.keys():
        book = pe.get_book(
            file_name=piezas[k]["nombre_archivo"],
            sheets=[piezas[k]["nombre_hoja"],]
            )
        for r in range(5, len(book[piezas[k]["nombre_hoja"]])):
            temp = {}
            for c in piezas[k]["columnas"].keys():
                valor = book[piezas[k]["nombre_hoja"]][r, piezas[k]["columnas"][c]]
                if (c=="codigo" and len(valor)>8):
                    temp.update({c: valor[:-2]})
                else:
                    temp.update({c: valor})
            csvpiezas.append(temp)

    if os.path.exists(OUTPUT_ITEMS):
        try:
            os.remove(OUTPUT_ITEMS)
        except:
            pass
    output_file = pe.get_sheet(records=csvpiezas)
    output_file.save_as(OUTPUT_ITEMS)


if __name__ == "__main__":
    main.execute()
