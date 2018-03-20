import unittest
from Lista import Lista

class TestCreateLista(unittest.TestCase):

    def test_crear_solo_nombre(self):
        nombre = 'Nombre Lista'
        lista = Lista(nombre)
        assert lista is not None
        self.assertEqual(lista.nombre, nombre)
        self.assertEqual(lista.publica, False)
        self.assertEqual(lista.genero, [])
        self.assertEqual(lista.descripcion, None)

    def test_crear_nombre_publica(self):
        nombre = 'Nombre Lista'
        lista = Lista(nombre, publica=True)
        assert lista is not None
        self.assertEqual(lista.nombre, nombre)
        self.assertEqual(lista.publica, True)
        self.assertEqual(lista.genero, [])
        self.assertEqual(lista.descripcion, None)




