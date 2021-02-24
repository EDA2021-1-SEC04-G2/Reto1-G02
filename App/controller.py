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


"""
El controlador se encarga de mediar entre la vista y el modelo.
"""


# Inicialización del Catálogo de libros

def init_catalog(list_type):
    catalog = model.new_catalog(list_type)
    return catalog


# Funciones para la carga de datos


def load_data(catalog):
  
    load_videos(catalog)
    load_categories(catalog)


def load_videos(catalog):
  
    videosfile = cf.data_dir + 'videos/videos-large.csv'
    input_file = csv.DictReader(open(videosfile, encoding='utf-8'))
    for video in input_file:
        model.add_video(catalog, video)


def load_categories(catalog):
    """
    Carga la información que asocia tags con libros.
    """
    categoriesfile = cf.data_dir + 'videos/category-id.csv'
    input_file = csv.DictReader(open(categoriesfile, encoding='utf-8'), delimiter='\t')
    for category in input_file:
        model.add_category(catalog, category)

def sort_videos(catalog,size,algorithm_type_number):
    if algorithm_type_number==1:
        algorithm_type='shell'
    if algorithm_type_number==2:
        algorithm_type='insertion'
    else:
        algorithm_type='selection'
    return model.sort_videos(catalog,size,algorithm_type)
        