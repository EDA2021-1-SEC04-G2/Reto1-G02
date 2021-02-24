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

def print_menu():
    print("Bienvenido")
    print("1- Cargar información en el catálogo")
    print("2- Ordenar videos por vistas")
    print("3- Encontrar mejores videos por categoría y país ")
    print("4- Encontrar videos tendencia por país")
    print("5- Encontrar videos tendencia por categoría")
    print("6- Encontrar videos con más likes")
    print("0- Salir")

def init_catalog(list_type_number):
    """
    Inicializa el catalogo de videos
    """
    if list_type_number==1:
        list_type="ARRAY_LIST"
    else:
        list_type="SINGLE_LINKED"
    return controller.init_catalog(list_type)


def load_data(catalog):
    """
    Carga los libros en la estructura de datos
    """
    controller.load_data(catalog)


def print_results(ord_videos, sample=10):
    size = lt.size(ord_videos)
    if size > sample:
        print("Los primeros ", sample, " videos ordenados son:")
        i=1
        while i <= sample:
            video = lt.getElement(ord_videos,i)
            print('Titulo: ' + video['title'] + ' Canal: '+video['channel_title']+' Vistas: '+video['views'])
            i+=1


catalog = None

"""
Menu principal
"""
while True:
    print_menu()
    inputs = input('Seleccione una opción para continuar\n')
    if int(inputs[0]) == 1:
        print('Tipos de lista:')
        print('1- Arreglo')
        print('2- Simplimente encadenada')
        list_type_number=int(input('Escoja que tipo de lista desea usar para cargar los datos del catálogo: '))
        print("Cargando información de los archivos ....")
        catalog = init_catalog(list_type_number)
        load_data(catalog)
        print('Se cargaron: ',lt.size(catalog['videos']), ' videos')
    elif int(inputs[0]) == 2:
        size = input("Indique tamaño de la muestra: ")
        print('Tipos de algoritmos:')
        print('1- Shell sort')
        print('2- Insertion sort')
        print('3- Selection sort')
        algorithm_type_number=int(input('Escoja el tipo de algoritmo que desea usar para ordenar los videos: '))
        print("Ordenando videos por vistas...")
        result = controller.sort_videos(catalog, int(size),algorithm_type_number)
        print("Para la muestra de", size, " elementos, el tiempo (mseg) es: ",
                                          str(result[0]))
        print_results(result[1])
    elif int(inputs[0]) == 3:
        pass
    elif int(inputs[0]) == 4:
        pass
    elif int(inputs[0]) == 5:
        pass
    else:
        sys.exit(0)
sys.exit(0)

