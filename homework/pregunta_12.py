"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_12():
    """
    Genere un diccionario que contengan como clave la columna 1 y como valor
    la suma de los valores de la columna 5 sobre todo el archivo.

    Rta/
    {'A': 177, 'B': 187, 'C': 114, 'D': 136, 'E': 324}

    """
    with open("files/input/data.csv", "r") as file:
        registers = {}
        for line in file:
            columns = line.split("\t")
            letter = columns[0]
            col5_values = columns[4].strip().split(",")
            sum = 0
            for elem in col5_values:
                value = int(elem.split(":")[1])
                sum += value
            if letter in registers:
                registers[letter] += sum
            else:
                registers[letter] = sum
    return dict(sorted(registers.items()))
