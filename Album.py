class Album(object):
	"""docstring for Album"""
	def __init__(self, nombre, fechaPublicacion, genero, descripcion):
		self._nombre = nombre
		self._fechaPublicacion = fechaPublicacion
		self._genero = genero [] #No se si esta bien declarado
		self._descripcion = descripcion


	def agregarGenero(self):
		pass

	def getAlbumsSimilares(self):
		pass

	def setAlbumsSimilares(self):
		pass
	
	def getPlaysCanciones(self):
		pass

	def setPlaysCanciones(self):
		pass