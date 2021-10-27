"""
 * Copyright 2020, Departamento de sistemas y Computación,
 * Universidad de Los Andes
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
 *
 * Contribuciones:
 *
 * Dario Correal - Version inicial
 """


import config as cf
from DISClib.ADT import list as lt
from DISClib.ADT import orderedmap as om
from DISClib.ADT import map as mp
from DISClib.DataStructures import mapentry as me
from DISClib.Algorithms.Sorting import shellsort as sa
import datetime
assert cf

"""
Se define la estructura de un catálogo de videos. El catálogo tendrá dos listas, una para los videos, otra para las categorias de
los mismos.
"""
def newCatalog():

    catalog={
          "UFOS":None,
          "Cities":None,
          "Duration":None,
          "HourMin":None,
          "Date":None,
          "Longitude":None
         }
    catalog['UFOS']= lt.newList('SINGLE_LINKED')
#Req 1
    catalog["Cities"]=mp.newMap(19901,
                           maptype="PROBING",
                           loadfactor=0.5,
                           comparefunction=compareCities)
#Req 2
    catalog["Duration"]=om.newMap(omaptype="RBT",
                                  comparefunction=compareSec)
#Req 3
    catalog["HourMin"]=om.newMap(omaptype="RBT",
                                 comparefunction=compareTime)
#Req 4
    catalog["Date"]=om.newMap(omaptype="RBT",
                              comparefunction=compareDates)
#Req 5
    catalog["Longitude"]=om.newMap(omaptype="RBT",
                                   comparefunction=compareLongitudes)
    return catalog

#def compareufos (ufo1,ufo2):

#comparefunction req 1
def compareCities (keycity,city):
    cityentry=me.getKey(city)
    if (keycity==cityentry):
        return 0
    elif (keycity>cityentry):
        return 1
    else:
        return -1

#comparefunction req 2
def compareSec(Sec1, Sec2):
    if (Sec1==Sec2):
        return 0
    elif (Sec1 > Sec2):
        return 1
    else:
        return -1

#comparefunction req 3
def compareTime(Time1, Time2):
    if (Time1==Time2):
        return 0
    elif (Time1 > Time2):
        return 1
    else:
        return -1
    
#comparefunction req 4
def compareDates(Date1, Date2):
    if (Date1==Date2):
        return 0
    elif (Date1 > Date2):
        return 1
    else:
        return -1

#comparefunction req 5
def compareLongitudes(Long1, Long2):
    if (Long1==Long2):
        return 0
    elif (Long1 > Long2):
        return 1
    else:
        return -1

# Funciones para agregar informacion al catalogo
def addufos(catalog, ufos):
    ufo={
        "datetime":ufos["datetime"],
        "city":ufos["city"],
        "state":ufos["state"],
        "country":ufos["country"],
        "shape":ufos["shape"],
        "duration (seconds)":ufos["duration (seconds)"],
        "duration (hours/min)":ufos["duration (hours/min)"],
        "comments":ufos["comments"],
        "date posted":ufos["date posted"],
        "latitude":ufos["latitude"],
        "longitude":ufos["longitude"]
        }
    lt.addLast(catalog["UFOS"],ufo)


#agregar información al indice del req1
def addcities(tablecity,city,ufos):
    try:
        if city != "" and mp.contains(tablecity,city)==False:
            ufoslist=lt.newList("ARRAY_LIST")
            lt.addLast(ufoslist,ufos)
            mp.put(tablecity,city,ufoslist)
        elif mp.contains(tablecity,city)==True:
            temp=mp.get(tablecity,city)
            temp=me.getValue(temp)
            lt.addLast(temp,ufos)
    except Exception as e:
        raise e

# Construccion de modelos

# Funciones para creacion de datos

# Funciones de consulta

# Funciones utilizadas para comparar elementos dentro de una lista

# Funciones de ordenamiento
