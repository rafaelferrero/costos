# Author: Rafael E. Ferrero

"""
    This program receive an Excel file and extract specific data into .csv file
"""


import os
import pyexcel as pe  # http://docs.pyexcel.org/
from datetime import datetime as dt
from hashbang import command
from sys import exit
from settings import (
    OUTPUT_PATH,
    OUTPUT_WA,
    OUTPUT_ITEMS,
    piezas,
    workareas,
    )


def get_str_timestamp():
    return str(dt.now())


def logerror(mensaje):
    with open(OUTPUT_PATH + "error_exportacion.txt", "a") as f:
        f.write("<<<" + get_str_timestamp() + ">>>   "+ mensaje + "\n")


def makemsg(file_name="", number_row=0, field_name="", field_value=""):
    msg = "Error en el archivo {}, ".format(file_name)
    msg += "fila numero {}, ".format(number_row)

    if not field_name:
        msg += "No indica el nombre del campo "
    else:
        msg += "en el campo '{}'', ".format(field_name)

    if not field_value:
        msg += "No indica el valor "
    else:
        msg += "el valor es '{}', ".format(field_value)
    msg += "y debería ser un valor numerico mayor a cero"

    return(msg)


@command
def main():
    # Proceso de archivo de costos de Work Areas
    logerror("Iniciamos un nuevo proceso!!!")
    try:
        wabook = pe.get_book(
            file_name=workareas["work_areas"]["nombre_archivo"],
            sheets=[workareas["work_areas"]["nombre_hoja"],]
        )
    except:
        logerror("No se encuentra el archivo {}".format(
            workareas["work_areas"]["nombre_archivo"]
        ))
        logerror("Finalizado con errores graves. NO ENVIAR CSV!!!")
        exit(2)

    csvwa = []
    for r in range(
            workareas["work_areas"]["linea_inicial"],
            len(wabook[workareas["work_areas"]["nombre_hoja"]])):

        temp = {}
        for c in workareas["work_areas"]["columnas"].keys():
            flag = True
            valor = wabook[
                workareas["work_areas"]["nombre_hoja"]][
                    r, workareas["work_areas"]["columnas"][c]]

            try:
                if not valor:
                    flag = False
                elif (c=="costo" and not float(valor)):
                    flag = False
                elif (c=="costo" and float(valor)<0):
                    flag = False
            except:
                flag = False

            if c=="codigo":
                temp.update({c: valor[11:-6]})
            else:
                temp.update({c: valor})

        if flag:
            csvwa.append(temp)
        else:
            logerror(makemsg(
                file_name=workareas["work_areas"]["nombre_archivo"],
                number_row=r+1,
                field_name=c,
                field_value=valor
            ))

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
        try:
            book = pe.get_book(
                file_name=piezas[k]["nombre_archivo"],
                sheets=[piezas[k]["nombre_hoja"],]
                )
        except:
            logerror("No se encuentra el archivo {}".format(
                workareas["work_areas"]["nombre_archivo"]
            ))
            logerror("Finalizado con errores graves. NO ENVIAR CSV!!!")
            exit(2)

        for r in range(
            piezas[k]["linea_inicial"], len(book[piezas[k]["nombre_hoja"]])):
            temp = {}
            for c in piezas[k]["columnas"].keys():
                flag = True
                valor = book[
                    piezas[k]["nombre_hoja"]][r, piezas[k]["columnas"][c]]

                try:
                    if not valor:
                        flag = False
                    elif (c=="costo" and not float(valor)) :
                        flag = False
                    elif (c=="costo" and float(valor)<0):
                        flag = False
                except:
                    flag = False

                if (c=="codigo" and len(valor)>8):
                    temp.update({c: valor[:-2]})
                else:
                    temp.update({c: valor})

            if flag:
                csvpiezas.append(temp)
            else:
                logerror(makemsg(
                    file_name=piezas[k]["nombre_archivo"],
                    number_row=r+1,
                    field_name=c,
                    field_value=valor
                ))

    if os.path.exists(OUTPUT_ITEMS):
        try:
            os.remove(OUTPUT_ITEMS)
        except:
            pass
    output_file = pe.get_sheet(records=csvpiezas)
    output_file.save_as(OUTPUT_ITEMS)
    logerror("Finalizamos el proceso!!!")

if __name__ == "__main__":
    main.execute()
