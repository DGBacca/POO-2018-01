import re

class User(object):
    """docstring for User"""
    lista_usuarios = []

    def __init__(self, password, email):
        self.password = password
        self.email = email

    @property
    def password(self):
        return self._password
    @property
    def email(self):
        return self._email
    @property
    def listas(self):
        return self._listas

    @password.setter
    def password(self, password):
        if password and not password.isspace():
            self._password = password
        else:
            raise Exception("Debe ingresar una password")

    @email.setter
    def email(self, email):
        if re.match(r"[^@]+@[^@]+\.[^@]+", email):
            self._email = email
        else:
            raise Exception("Email con el formato equibocado")

    @listas.setter
    def listas(self, lista):
        self._listas = lista

    def registrar_usuario(self):
        User.lista_usuarios.append(self)

    def eliminarUsuario(self):
            pass

    def AutenticarUsuario(self):
            pass
