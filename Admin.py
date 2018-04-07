import User from User
class Admin(User):
	"""docstring for Admin"""
	def __init__(self,identificacion,username,password,email):
		super().__init__(username,email,password)
		self._identificacion= identificacion


	def enviarNotificacion(self):
		pass
