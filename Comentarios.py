class Comentarios(object):
    """docstring for Comentarios"""
    def __init__(self, titulo, contenido):
        self.titulo = titulo
        self.contenido = contenido
        comentarios = []

    @property
    def titulo(self): return self._titulo

    @property
    def contenido(self): return self._contenido

    @titulo.setter
    def titulo(self, titulo):
        self._titulo = titulo

    @contenido.setter
    def contenido(self, contenido):
        self._contenido = contenido

    def responder(self):
