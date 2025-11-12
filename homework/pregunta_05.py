"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_05():
    """
    Retorne una lista de tuplas con el valor maximo y minimo de la columna 2
    por cada letra de la columa 1.

    Rta/
    [('A', 9, 2), ('B', 9, 1), ('C', 9, 0), ('D', 8, 3), ('E', 9, 1)]

    """
    with open("files/input/data.csv", "r") as file:
        corr = {"A":0,
                "B":1,
                "C":2,
                "D":3,
                "E":4}
        max = [0] * len(sorted(corr))
        min = [float("inf")] * len(sorted(corr))
        for line in file:
            columns = line.split("\t")
            reg = corr[columns[0]]
            if max[reg] < int(columns[1]):
                max[reg] = int(columns[1])
            if min[reg] > int(columns[1]):
                min[reg] = int(columns[1])

        result = []
        for register in corr.items():
            c = register[1]
            result.append((register[0],max[c],min[c]))
    return sorted(result)
