﻿"""
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
import time
import sys
import controller
from DISClib.ADT import list as lt
assert cf
from DISClib.ADT import map as mp
from DISClib.DataStructures import mapentry as me
from DISClib.ADT import orderedmap as om
import datetime as dt

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
        catalog=controller.initcatalog()
        controller.loaddata(catalog)
        
        
    elif int(inputs[0]) == 1:
        city=input("ingrese la ciudad a buscar: ")
        index= catalog["Cities"]
        ciudades= lt.size(mp.keySet(index))
        print("\nhay "+str(ciudades)+" ciudades reportadas con avistamientos")

        entry= mp. get(index,city)
        value= me.getValue(entry)
        print("\nse han reportado "+str(value["count"])+ " avistamientos en "+city)
        print("\los primeros tres y los ultimos tres avistamientos reportados son: ")
        ufos= om.valueSet(value["datetime"])

        nuevaLista= lt.newList("ARRAY_LIST")
        for lista in lt.iterator(ufos):
            for ufo in lt.iterator(lista):
                lt.addLast(nuevaLista,ufo)

        i= 1
        while i <= 3:
            ufo= lt.getElement(nuevaLista, i)
            
            print("Fecha: "+ufo["datetime"]+
                  ". Ciudad: " +ufo["city"]+
                  ". Pais: " +ufo["country"]+
                  ". Duración en segundos: " +ufo["duration (seconds)"]+
                  ". Forma del objeto: " +ufo["shape"])
            i+=1
        
        i=-2
        while i <= 0:
            ufo= lt.getElement(nuevaLista, i)
            print("Fecha: "+ufo["datetime"]+
                  ". Ciudad: " +ufo["city"]+
                  ". Pais: " +ufo["country"]+
                  ". Duración en segundos: " +ufo["duration (seconds)"]+
                  ". Forma del objeto: " +ufo["shape"])
            i+=1


    elif int(inputs[0]) ==2:
        seg_min=float(input("Ingrese el número de segundos en donde desea que empiece el rango: "))
        seg_max=float(input("Ingrese el número de segundos en donde desea que termine el rango: "))
        total_sightings=controller.longduration(catalog)
        list_range=controller.sightings_in_range(catalog, seg_min, seg_max)
        print("El total de avistamientos registrados con duración máxima en el rango es: ")
        print(total_sightings)
        print("La información de los tres primeros y ultimos avistamientos dentro del rango de duración son: ")
        for element in lt.iterator(list_range[0]):
                print("Fecha y hora: "+element["datetime"]+
                          ". Ciudad: "+element["city"]+
                          ". Pais: "+element["country"]+
                          ". Duración en segundos: "+ element["duration (seconds)"]+
                          ". Forma del objeto: "+element["shape"])
        for element in lt.iterator(list_range[1]):
                print("Fecha y hora: "+element["datetime"]+
                          ". Ciudad: "+element["city"]+
                          ". Pais: "+element["country"]+
                          ". Duración en segundos: "+ element["duration (seconds)"]+
                          ". Forma del objeto: "+element["shape"])
    
    elif int(inputs[0]) ==3:
        index= catalog["HourMin"]
        antigua= om.minKey(index)
        avistamientos= lt.size(me.getValue(om.get(index,antigua)))
        print("avistamientos mas tardios: "+ str(avistamientos))

        limIn=input("Ingrese el limite inferior de hora: ")
        limSup=input("\nIngrese el limite superior de hora: ")

        dateIn= dt.time.fromisoformat(limIn)
        dateSup= dt.time.fromisoformat(limSup)

        sightings= om.values(index, dateIn, dateSup)
        nuevaLista= lt.newList("ARRAY_LIST")

        for lista in lt.iterator(sightings):
            for ufo in lt.iterator(lista):
                lt.addLast(nuevaLista,ufo)
        
        total= lt.size(nuevaLista)
        print("\nel total de avistamientos en el rango es de: "+str(total))

        print("\nlos primeros tres y los ultimos tres avistamientos reportados son: ")

        i= 1
        while i <= 3:
            ufo= lt.getElement(nuevaLista, i)
            
            print("Fecha: "+ufo["datetime"]+
                  ". Ciudad: " +ufo["city"]+
                  ". Pais: " +ufo["country"]+
                  ". Duración en segundos: " +ufo["duration (seconds)"]+
                  ". Forma del objeto: " +ufo["shape"])
            i+=1
        
        i=-2
        while i <= 0:
            ufo= lt.getElement(nuevaLista, i)
            print("Fecha: "+ufo["datetime"]+
                  ". Ciudad: " +ufo["city"]+
                  ". Pais: " +ufo["country"]+
                  ". Duración en segundos: " +ufo["duration (seconds)"]+
                  ". Forma del objeto: " +ufo["shape"])
            i+=1

    elif int(inputs[0]) ==4:
        index= catalog["Date"]
        antigua= om.minKey(index)
        avistamientos= lt.size(me.getValue(om.get(index,antigua)))
        print("el numero de avistamientos con fecha mas antigua es: "+ str(avistamientos))

        limIn=input("Ingrese el limite inferior de fecha: ")
        limSup=input("Ingrese el limite superior de fecha: ")

        dateIn= dt.datetime.fromisoformat(limIn)
        dateSup= dt.datetime.fromisoformat(limSup)

        sightings= om.values(index, dateIn, dateSup)
        nuevaLista= lt.newList("ARRAY_LIST")

        for lista in lt.iterator(sightings):
            for ufo in lt.iterator(lista):
                lt.addLast(nuevaLista,ufo)
        
        total= lt.size(nuevaLista)
        print("\nel total de avistamientos en el rango es de: "+str(total))

        print("\nlos primeros tres y los ultimos tres avistamientos reportados son: ")

        i= 1
        while i <= 3:
            ufo= lt.getElement(nuevaLista, i)
            
            print("Fecha: "+ufo["datetime"]+
                  ". Ciudad: " +ufo["city"]+
                  ". Pais: " +ufo["country"]+
                  ". Duración en segundos: " +ufo["duration (seconds)"]+
                  ". Forma del objeto: " +ufo["shape"])
            i+=1
        
        i=-2
        while i <= 0:
            ufo= lt.getElement(nuevaLista, i)
            print("Fecha: "+ufo["datetime"]+
                  ". Ciudad: " +ufo["city"]+
                  ". Pais: " +ufo["country"]+
                  ". Duración en segundos: " +ufo["duration (seconds)"]+
                  ". Forma del objeto: " +ufo["shape"])
            i+=1



    elif int(inputs[0]) ==5:
        longmin=input("Ingrese la longitud en donde desea que empiece el rango: ")
        longmax=input("Ingrese la longitud en donde desea que termine el rango: ")
        latmin=input("Ingrese la latitud en donde desea que empiece el rango: ")
        latmax=input("Ingrese la latitud en donde desea que termine el rango: ")
        list_range=controller.num_in_range(catalog, longmin, longmax, latmin, latmax)
        total_in_range=controller.total_in_area(list_range)
        sorted_list=controller.sorting_list(list_range)
        fivefirstlast=controller.fivefirstlast(sorted_list)
        print("El total de avistamientos en el area definida es de: ")
        print(total_in_range)
        print("La información de los cinco primeros y cinco últimos avistamientos dentro del rango es: ")
        if lt.size(sorted_list)<=10:
            for element in lt.iterator(sorted_list):
                print("Fecha y hora: "+element["datetime"]+
                          ". Ciudad: "+element["city"]+
                          ". Pais: "+element["country"]+
                          ". Duración en segundos: "+ element["duration (seconds)"]+
                          ". Forma del objeto: "+element["shape"]+
                          ". Longitud: "+element["longitude"]+
                          ". Latitud: "+element["latitude"])
        else:
            for element in lt.iterator(fivefirstlast[0]):
                print("Fecha y hora: "+element["datetime"]+
                          ". Ciudad: "+element["city"]+
                          ". Pais: "+element["country"]+
                          ". Duración en segundos: "+ element["duration (seconds)"]+
                          ". Forma del objeto: "+element["shape"]+
                          ". Longitud: "+element["longitude"]+
                          ". Latitud: "+element["latitude"])

            for element in lt.iterator(fivefirstlast[1]):
                print("Fecha y hora: "+element["datetime"]+
                          ". Ciudad: "+element["city"]+
                          ". Pais: "+element["country"]+
                          ". Duración en segundos: "+ element["duration (seconds)"]+
                          ". Forma del objeto: "+element["shape"]+
                          ". Longitud: "+element["longitude"]+
                          ". Latitud: "+element["latitude"])




        pass

    else:
        sys.exit(0)
sys.exit(0)











