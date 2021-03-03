# Author: Rafael E. Ferrero

"""
    This program receive an Excel file and extract specific data into .csv file
"""


import pyexcel as pe  # http://docs.pyexcel.org/
from datetime import datetime as dt
from settings import (
    OUTPUT_PATH,
    piezas,
    )


def main():
    export = []
    for k in piezas.keys():
        book = pe.get_book(
            file_name=piezas[k]["nombre_archivo"],
            sheets=[piezas[k]["nombre_hoja"],]
            )
        for r in range(5, len(book[piezas[k]["nombre_hoja"]])):
            temp = {}
            for c in piezas[k]["columnas"].keys():
                temp.update({
                    c: book[
                        piezas[k]["nombre_hoja"]][
                            r, piezas[k]["columnas"][c]]
                })
            export.append(temp)
    output_file = pe.get_sheet(records=export)
    output_file.save_as(OUTPUT_PATH + "costo-piezas.csv")


if __name__ == "__main__":
    main.execute()
