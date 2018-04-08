class Admin(object):
	"""docstring for Admin"""
	def __init__(self, identificacion):
		self._identificacion= identificacion



	def enviarNotificacion(self, email, title, text):
            notificacion = {
                    'title': title,
                    'text': text
            }

