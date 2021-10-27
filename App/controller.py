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
 """

import config as cf
import model
import csv
from DISClib.ADT import list as lt

"""
El controlador se encarga de mediar entre la vista y el modelo.
"""
# Inicialización del Catálogo de UFOS
def initcatalog():
    catalog=model.newCatalog()
    return catalog

# Funciones para la carga de datos
def loaddata(catalog):
    try:
        load_ufos(catalog)
        load_tables(catalog)
    except Exception as e:
        raise e

def load_ufos(catalog):
    ufosfile=cf.data_dir+"UFOS-utf8-small.csv"
    input_file=csv.DictReader(open(ufosfile,encoding="utf-8"), 
                              delimiter="," )
    for ufos in input_file:
        model.addufos(catalog,ufos)
    return catalog

def load_tables(catalog):
    for ufos in lt.iterator (catalog["UFOS"]):
        city=ufos["city"]
        tablecity=catalog["Cities"]
        model.addcities(tablecity,city,ufos)
    return catalog


# Inicialización del Catálogo de libros

# Funciones para la carga de datos

# Funciones de ordenamiento

# Funciones de consulta sobre el catálogo
