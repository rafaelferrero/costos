# Author: Rafael E. Ferrero

"""
    This program receive an Excel file and extract specific data into .csv file
"""


import pyexcel as pe  # http://docs.pyexcel.org/
from datetime import datetime as dt
from settings import (
    OUTPUT_FILE,
    archivos,
    )


def get_str_timestamp():
    return str(int(dt.timestamp(dt.now())))


def main():
    export = []
    for k in archivos.keys():
        book = pe.get_book(
            file_name=archivos[k]["nombre_archivo"],
            sheets=[archivos[k]["nombre_hoja"],]
            )
        for r in range(5, len(book[archivos[k]["nombre_hoja"]])):
            temp = {}
            for c in archivos[k]["columnas"].keys():
                temp.update({
                    c: book[
                        archivos[k]["nombre_hoja"]][
                            r, archivos[k]["columnas"][c]]
                })
            export.append(temp)
    output_file = pe.get_sheet(records=export)
    output_file.save_as(OUTPUT_FILE)


if __name__ == "__main__":
    main.execute()
