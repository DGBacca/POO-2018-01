import pandas as pd
import numpy as np
from Cancion import Cancion

class Lista(object):
    """docstring for Lista"""
    def __init__(self, nombre, creador,  genero=None, publica=False, descripcion=None):
        self.nombre = nombre
        self.publica = publica
        self.descripcion = descripcion
        self.creador = creador
        self.canciones = []

    @property
    def nombre(self): return self._nombre

    @property
    def publica(self): return self._publica

    @property
    def descripcion(self): return self._descripcion

    @property
    def creador(self): return self._creador

    @property
    def canciones: return self._canciones

    @nombre.setter
    def nombre(self, nombre): self._nombre = nombre

    @publica.setter
    def publica(self, publica):
        self._publica = not not publica

    @creador.setter
    def creador(self, creador):
        if creador:
            self._creador = creador
        else:
            raise ValueError("Creador Necesitado")


    @descripcion.setter
    def descripcion(self, descripcion): self._descripcion = descripcion

    @canciones.setter
    def canciones(self, canciones):
        self._canciones = canciones

    def crearLista(self):
        listas = pd.read_csv('listas.csv', index_col=0)
        query  = "nombre == @self.nombre"
        existe = listas.query(query).any()
        if existe.nombre:
            raise Exception("Lista ya existe, use otro nombre")
        campos = {
                'nombre':      [self.nombre],
                'publica':     [self.publica],
                'descripcion': [self.descripcion]
        }
        ag = pd.DataFrame(campos)
        listas = listas.append(ag, ignore_index=True)
        listas.to_csv('listas.csv')

    def eliminarLista(self):
        listas = pd.read_csv('listas.csv', index_col=0)
        listas = listas[listas.nombre != self.nombre]
        listas.to_csv('listas.csv')

    def modificarLista(self):
        listas = pd.read_csv('listas.csv', index_col=0)
        campos = {
                'nombre':      [self.nombre],
                'publica':     [self.publica],
                'descripcion': [self.descripcion]
        }
        ag = pd.DataFrame(campos)
        listas.update(ag)
        listas.to_csv('listas.csv')

    def agregarCancion(Cancion cancion):
        self.canciones.append(cancion)

    def eliminarCancion(Cancion cancion):
        self.canciones = [cancion_iter for cancion_iter in canciones if cancion_iter.id != cancion]
