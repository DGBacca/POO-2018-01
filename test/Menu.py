import sys
class Run():

	def __init__(self):
		self.choices = {
		"1": self.Administrador,
    "1.1": self. 'Ver usuarios'
    "1.2": self. ' Crear usuraio'
    "1.3": self. ' Eliminar Usuario'
    "1.4": self. ' Crear playlist'
    "1.5": self. ' Eliminar playlist'
    "1.6": self. ' Crear albúm'
    "1.7": self. ' Eliminar albúm'
    "1.8": self. ' Crear artista'
    "1.9": self. ' Eliminar artista'
    "1.10": self. ' Agregar comentario'
    "1.11": self. ' Eliminar comentario'
		"2": self.Usuario,
    "2.2": self. ' Eliminar playlist'
    "2.3": self. ' Crear comentario'
    "2.4": self. ' Eliminar comentario'
    "2.5": self. '. Salir'
		"3": self.Invitado,
    "3.1": self. '. Registrase'
    "3.2": self. '. Ver playlist'
    "3.3": self. '. Salir'
		"4": self.salir
       }

  MENU_ENTRADA="""
      CHEAPY Menu Principal
       1. Administrador
       2. Usuario
       3. Invitado
       4. Salir
       """

    def salir(self):
       print("Chaito")
       sys.exit(0)
       
    def run(self,menu = MENU_ENTRADA): 

       while self.break_while==1:
           #self.display_menu()
           print(menu)
           opcion = input("Ingrese una opcion: ")
           action = self.choices.get(opcion)
           if action:
               action()
           else:
               print("{0} no es una opcion valida".format(opcion))

    def Administrador(self):

    	menu_administrador = """
    	CHEAPY Menu Administrador
       	1.1. Ver usuarios
        1.2. Crear usuraio
        1.3. Eliminar Usuario
        1.4. Crear playlist
        1.5. Eliminar playlist
        1.6. Crear albúm
        1.7. Eliminar albúm
        1.8. Crear artista
        1.9. Eliminar artista
        1.10. Agregar comentario
        1.11. Eliminar comentario
        1.12. Salir

    		"""
    	self.run(menu_administrador)


    def Usuario(self):
      menu_usuario = """
      CHEAPY Menu Usuario
        2.1. Crear playlist
        2.2. Eliminar playlist
        2.3. Crear comentario
        2.4. Eliminar comentario
        2.5. Salir

        """

    def Invitado(self):
    	menu_invitado = """
      CHEAPY Menu Usuario
        3.1. Registrase
        3.2. Ver playlist
        3.3. Salir

        """
