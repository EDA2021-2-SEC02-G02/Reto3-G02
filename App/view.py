"""
 * Copyright 2020, Departamento de sistemas y Computación, Universidad
 * de Los Andes
 *
 *
 * Desarrolado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
 *
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along withthis program.  If not, see <http://www.gnu.org/licenses/>.
 """

import config as cf
import sys
import controller
from DISClib.ADT import list as lt
assert cf


"""
La vista se encarga de la interacción con el usuario
Presenta el menu de opciones y por cada seleccion
se hace la solicitud al controlador para ejecutar la
operación solicitada
"""
ufosfile="UFOS-utf8.csv"
def printMenu():
    print("Bienvenido")
    print("0- Crear y cargar información en el catálogo")
    print("1- Contar los avistamientos de Ovnis en una ciudad")
    print("2- Contar los avistamientos de Ovnis por duración")
    print("3- Contar avistamientos de Ovnispor Hora/Minutos del día")
    print("4- Contar los avistamientos de Ovnis en un rango de fechas")
    print("5- Contar los avistamientos de Ovnis de una Zona Geográfica")

catalog = None

"""
Menu principal
"""
while True:
    printMenu()
    inputs = input('Seleccione una opción para continuar\n')
    if int(inputs[0]) == 0:
        print("Creando y cargando información del archivo ....")
        cont=controller.initcatalog()
        controller.loaddata(cont)
        controller.load_ufos(cont)
        print("se imprime la altura y el número de elementos del requerimiento 2")
        print("Altura del arbol: "+str(controller.req2indexHeight(cont)))
        print("Elementos en el arbol: "+ str(controller.req2indexSize(cont)))

    elif int(inputs[0]) == 1:
        pass

    else:
        sys.exit(0)
sys.exit(0)











