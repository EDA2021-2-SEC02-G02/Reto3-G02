﻿"""
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
from DISClib.Algorithms.Sorting import mergesort as mg
import datetime as dt
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
    updateDuration(catalog["Duration"],ufo)
    updateLongitude(catalog["Longitude"], ufo)


#agregar informacion al indice del req1
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


#agregar informacion al indice del req2
def updateDuration(tree, ufo):
    occurredduration=float(ufo["duration (seconds)"])
    entry=om.get(tree,occurredduration)
    if entry is None:
        durationentry=lt.newList("ARRAY_LIST")
        om.put(tree,occurredduration,durationentry)
    else:
        durationentry=me.getValue(entry)
    lt.addLast(durationentry,ufo)
    return tree

#def req2indexSize(catalog):
 #   return om.size(catalog["Duration"])

#agregar informacion al indice del req5
def updateLongitude(tree, ufo):
    occurredlongitude=(round(float(ufo["longitude"]),2))
    entry=om.get(tree,occurredlongitude)
    if entry is None:
        longitudeentry=newLatitudetree(ufo)
        om.put(tree,occurredlongitude,longitudeentry)
    else:
        longitudeentry=me.getValue(entry)
    addLatitudevalue(longitudeentry,ufo)
    return tree

def newLatitudetree(ufo):
    latitudes={}
    latitudes["latitudeindex"]=om.newMap (omaptype="RBT",
                                  comparefunction=compareLatitudes)
    return latitudes
    
def addLatitudevalue(tree, ufo):
    tree=tree["latitudeindex"]
    occurredlatitude=(round(float(ufo["latitude"]),2))
    entry=om.get(tree,occurredlatitude)
    if entry is None:
        latitudeentry=lt.newList("ARRAY_LISY")
        om.put(tree,occurredlatitude,latitudeentry)
    else:
        latitudeentry=me.getValue(entry)
    lt.addLast(latitudeentry,ufo)
    return tree

def compareLatitudes (Lati1, Lati2):
    if (Lati1==Lati2):
        return 0
    elif (Lati1 > Lati2):
        return 1
    else:
        return -1



# Funciones de consulta
#Req1, crear arbol por la ciudad entrada por parametro
def createtreecity(catalog, city):
    citytable=catalog["Cities"]

#Req2,Contar los avistamientos por duración
#número de avistamientos con la duración más larga
def longduration (catalog):
    durationtree=catalog["Duration"]
    maxduration=om.maxKey(durationtree)
    key_value=om.get(durationtree,maxduration)
    lst=me.getValue(key_value)
    numviews=lt.size(lst)
    return numviews

#mostrar avistamientos en un rango de duración
def sightings_in_range(catalog, segmin, segmax):
    durationtree=catalog["Duration"]
    range=om.values(durationtree,segmin,segmax)
    list_answer=lt.newList("ARRAY_LIST")
    for lst in lt.iterator(range):
        for sightings in lt.iterator(lst):
            lt.addLast(list_answer,sightings)
    firstthree=lt.subList(list_answer,1,3)
    lastthree=lt.subList(list_answer,(lt.size(list_answer)-2),3)
    return firstthree, lastthree

#Req 5.Contar los avistamientos de una Zona Geográfica

def num_in_range(catalog, longmin, longmax, latmin, latmax):
    longitudetree=catalog["Longitude"]
    longituderange=om.values(longitudetree,longmin,longmax)
    lst_in_range=lt.newList("ARRAY_LIST")
    for longitude in lt.iterator(longituderange):
        latituderange=om.values(longitude,latmin,latmax)
        if lt.size(latituderange)>1:
            for elem in latituderange:
                lt.addLast(lst_in_range,elem)
        else:
            lt.addLast(lst_in_range,latituderange)
    return lst_in_range

def total_in_area(lst_in_range):
    size=lt.size(lst_in_range)
    return size

def sorting_list(lst_in_range):
    sorted_list=mg.sort(lst_in_range, cmpBylongitude)
    return sorted_list

def cmpBylongitude(longitude1, longitude2):
    if longitude1["longitude"]!="" and longitude2["longitude"]!="":
        long1=longitude1["longitude"]
        long2=longitude2["longitude"]
        return long1<long2

def fivefirstlast(sorted_list):
    fivefirst=lt.subList(sorted_list,1,5)
    fivelast=lt.subList(sorted_list,(lt.size(sorted_list)-4),5)
    return fivefirst,fivelast