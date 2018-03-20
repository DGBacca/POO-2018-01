class Lista(object):
    """docstring for Lista"""
    def __init__(self, nombre, genero=None, publica=False, descripcion=None):
        self.nombre = nombre
        self.genero = genero or []
        self.publica = publica
        self.descripcion = descripcion

    @property
    def nombre(self): return self._nombre

    @property
    def publica(self): return self._publica

    @property
    def genero(self): return self._genero

    @property
    def descripcion(self): return self._descripcion

    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre

    @publica.setter
    def publica(self, publica): self._publica = publica

    @genero.setter
    def genero(self, genero): self._genero = genero

    @descripcion.setter
    def descripcion(self, descripcion): self._descripcion = descripcion

    def crearLista(self):
	    pass

    def eliminarLista(self):
	    pass

    def agregarCategoria(self):
	    pass

    def removerCategoria(self):
	    pass

    def compartir(self):
	    pass
