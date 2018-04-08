import unittest
import pandas as pd
from Lista import Lista

class TestCreateLista(unittest.TestCase):

    def setUp(self):
        f = open('listas.csv', 'w+')
        f.write(",descripcion,nombre,publica")
        f.close()

    def tearDown(self):
        import os
        os.remove('listas.csv')

    def test_crear_solo_nombre(self):
        nombre = 'Nombre Lista'
        creador = 'usuario'
        lista = Lista(nombre, creador=creador)
        assert lista is not None
        self.assertEqual(lista.nombre, nombre)
        self.assertEqual(lista.publica, False)
        self.assertEqual(lista.descripcion, None)

    def test_crear_nombre_publica(self):
        nombre = 'Nombre Lista'
        creador = 'usuario'
        lista = Lista(nombre, publica=True, creador=creador)
        assert lista is not None
        self.assertEqual(lista.nombre, nombre)
        self.assertEqual(lista.publica, True)
        self.assertEqual(lista.descripcion, None)

    def test_crear_lista(self):
        nombre = 'Nombre Lista'
        publica = False
        descripcion = 'Descripcion del Lista'
        creador = 'usuario'
        lista = Lista(nombre=nombre, publica=publica, descripcion=descripcion, creador=creador)
        lista.crearLista()
        lista_file = pd.read_csv('listas.csv', index_col=0).iloc[0]
        self.assertEqual(lista_file.nombre, nombre)
        self.assertEqual(lista_file.publica, publica)
        self.assertEqual(lista_file.descripcion, descripcion)

    def test_eliminar_list(self):
        nombre = 'Nombre Lista'
        publica = False
        descripcion = 'Descripcion del Lista'
        creador = 'usuario'
        lista = Lista(nombre=nombre, publica=publica, descripcion=descripcion, creador=creador)
        # lista.crearLista()
        lista.eliminarLista()
        lista_file = pd.read_csv('listas.csv', index_col=0)
        self.assertEqual(lista_file.empty, True)

    def test_modificar_lista(self):
        nombre = 'Nombre Lista'
        publica = False
        descripcion = 'Descripcion del Lista'
        creador = 'usuario'
        lista = Lista(nombre=nombre, publica=publica, descripcion=descripcion, creador=creador)

        lista.crearLista()
        lista_file = pd.read_csv('listas.csv', index_col=0).iloc[0]
        descripcion_modificado = 'Descripcion de la lista modificada'
        lista.descripcion = descripcion_modificado
        lista.modificarLista()
        lista_file = pd.read_csv('listas.csv', index_col=0).iloc[0]
        self.assertEqual(lista_file.nombre, nombre)
        self.assertEqual(lista_file.publica, publica)
        self.assertEqual(lista_file.descripcion, descripcion_modificado)

        lista.eliminarLista()
        lista_file = pd.read_csv('listas.csv', index_col=0)
        self.assertEqual(lista_file.empty, True)



