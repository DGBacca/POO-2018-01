import re
import pandas as pd
import numpy as np

class User(object):
    """docstring for User"""
    def __init__(self, email, password):
        self.password = password
        self.email = email
        self.listas = []

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
        lista_usuarios = pd.read_csv('usuarios.csv', index_col=0)
        query = 'email == @self.email'
        user_auth = lista_usuarios.query(query).any()
        if(user_auth.email):
            raise Exception("Usuario ya existe")

        campos = {'email': self.email,
                'password': self.password,
                'listas': ','.join(self.listas)}
        lista_usuarios = lista_usuarios.append(campos, ignore_index=True)
        lista_usuarios.to_csv('usuarios.csv')

    def guardar_usuario(self):
        if not User.AutenticarUsuario(self.email, self.password):
            raise Exception("Usuario no existe")

        lista_usuarios = pd.read_csv('usuarios.csv', index_col = 0)
        campos = {'email':  [self.email],
                'password': [self.password],
                'listas':   [','.join(self.listas)]}
        user_update = pd.DataFrame(campos)
        lista_usuarios.update(user_update)
        lista_usuarios.to_csv('usuarios.csv')


    def eliminarUsuario(self):
        lista_usuarios = pd.read_csv('usuarios.csv', index_col=0)
        lista_usuarios = lista_usuarios[lista_usuarios.email != self.email]
        lista_usuarios.to_csv('usuarios.csv')


    @staticmethod
    def AutenticarUsuario(email, password):
        # import ipdb; ipdb.set_trace()
        query = 'email == @email & password == @password'
        lista_usuarios = pd.read_csv('usuarios.csv', index_col=0)
        user_auth = lista_usuarios.query(query)
        auth = user_auth.any()
        if auth.email and auth.password:
            user = User(user_auth.email[0], user_auth.password[0])
            lista = user_auth.listas[0]
            user.listas = lista.split(',') if str(lista) != 'nan' else []
            return user
        return None
