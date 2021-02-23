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
from DISClib.Algorithms.Sorting import shellsort as sa
assert cf

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
               'categories': None,
               'countries': None,
               'categories_countries': None,
               'tags': None}

    catalog['videos'] = lt.newList(list_type)
    catalog['categories'] = lt.newList(list_type)
    catalog['countries'] = lt.newList(list_type)
    catalog['tags'] = lt.newList(list_type)
    return catalog

# Funciones para agregar informacion al catalogo

def add_video(catalog, video):
    lt.addLast(catalog['videos'], video)


def add_category(catalog, category):
    lt.addLast(catalog['categories'], category)

# Funciones para creacion de datos

def new_categories(name,id):
    """
    Crea una nueva estructura para modelar los libros de
    un autor y su promedio de ratings
    """
    category = {'name': "", "videos": None,"id": ""}
    category['name'] = name
    category['id'] = id
    category['videos'] = lt.newList('ARRAY_LIST')
    return category


