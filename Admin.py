from User import User
class Admin(User):
	"""docstring for Admin"""
	def __init__(self,identificacion,username,password,email):
		super().__init__(username,email,password)
		self._identificacion= identificacion


<<<<<<< HEAD

	def enviarNotificacion(self, email, title, text):
            notificacion = {
                    'title': title,
                    'text': text
            }

=======
	def enviarNotificacion(self):
		pass
>>>>>>> f2c063f571c0228c942691dae341c65d71aa16d3
