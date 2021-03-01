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
import time
import sys
from DISClib.ADT import list as lt
from DISClib.Algorithms.Sorting import shellsort as shell
from DISClib.Algorithms.Sorting import insertionsort as insertion
from DISClib.Algorithms.Sorting import selectionsort as selection
from DISClib.Algorithms.Sorting import quicksort as quick
from DISClib.Algorithms.Sorting import mergesort as merge
assert cf
default_limit=1000
sys.setrecursionlimit(default_limit*1000)
"""
Se define la estructura de un catálogo de videos. El catálogo tendrá dos listas, una para los videos, otra para las categorias de
los mismos.
"""
# Construccion de modelos

def new_catalog(list_type):
    """
    Inicializa el catálogo de libros. Crea una lista vacia para guardar
    todos los libros, adicionalmente, crea una lista vacia para los autores,
    una lista vacia para los generos y una lista vacia para la asociación
    generos y libros. Retorna el catalogo inicializado.
    """
    catalog = {'videos':None,
               'categories': None}

    catalog['videos'] = lt.newList(list_type)
    catalog['categories'] = lt.newList(list_type)
    return catalog

# Funciones para agregar informacion al catalogo

def add_video(catalog, video):
    lt.addLast(catalog['videos'], video)


def add_category(catalog, category):
    lt.addLast(catalog['categories'], category)

# Funciones para creacion de datos

#Funciones de comparación

def cmp_videos_by_views(video1,video2):
    return float(video1['views'])>float(video2['views'])

# Funciones de ordenamiento

def sort_videos(catalog, size, algorithm_type):
    size=min(size,lt.size(catalog['videos']))
    sub_list = lt.subList(catalog['videos'], 1, size)
    sub_list = sub_list.copy()
    start_time = time.process_time()
    if algorithm_type=='shell':
        sorted_list=shell.sort(sub_list, cmp_videos_by_views)
    if algorithm_type=='insertion':
        sorted_list=insertion.sort(sub_list, cmp_videos_by_views)
    if algorithm_type=='selection':
        sorted_list=selection.sort(sub_list, cmp_videos_by_views)
    if algorithm_type=='quick':
        sorted_list=quick.sort(sub_list, cmp_videos_by_views)
    if algorithm_type=='merge':
        sorted_list=merge.sort(sub_list, cmp_videos_by_views)
    stop_time = time.process_time()
    elapsed_time_mseg = (stop_time - start_time)*1000
    return elapsed_time_mseg, sorted_list 