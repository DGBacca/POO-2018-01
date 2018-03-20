from User import User
import unittest

class TestUserCreation(unittest.TestCase):

    def test_user_creation_all_data_given_properly(self):
        password = 'password'
        email = 'username1@email.com'
        user = User(password, email)
        assert user is not None

    def test_user_creation_not_proper_email_raise_error(self):
        password = 'password'
        email = 'username1email.com'
        with self.assertRaises(Exception) as context:
            user = User(password, email)
        self.assertTrue('Email con el formato equivocado', str(context.exception))

    def test_user_creation_no_password(self):
        email = 'username1@email.com'
        # No password
        password = ''
        with self.assertRaises(Exception) as context:
            user = User(password, email)
        self.assertTrue('Debe ingresar una password', str(context.exception))
        # password espacios
        password = ' '
        with self.assertRaises(Exception) as context:
            user = User(password, email)
        self.assertTrue('Debe ingresar una password', str(context.exception))
        # password tabs
        password = '\t'
        with self.assertRaises(Exception) as context:
            user = User(password, email)
        self.assertTrue('Debe ingresar una password', str(context.exception))

class TestUserRegistration(unittest.TestCase):

    def test_user_registration(self):
        password = 'password'
        email = 'user@email.com'
        user = User(password, email)
        user.registrar_usuario()
        self.assertTrue(user in User.lista_usuarios)

    def test_user_registration_repeated_email(self):
        password = 'password'
        email = 'user1@email.com'
        user1 = User(password, email)
        user2 = User(password, email)
        user1.registrar_usuario()
        self.assertTrue(user1 in User.lista_usuarios)
        with self.assertRaises(Exception) as context:
            user2.registrar_usuario()
        self.assertEqual('Email en uso', str(context.exception))


class TestUserDelition(unittest.TestCase):

    def setUp(self):
        password = 'password'
        email1 = 'user1@email.com'
        email2 = 'user2@email.com'
        email3 = 'user3@email.com'
        user1 = User(password, email1)
        user2 = User(password, email2)
        user3 = User(password, email3)
        user1.registrar_usuario()
        user2.registrar_usuario()
        user3.registrar_usuario()

    def test_borrar_usuario(self):
        pass


