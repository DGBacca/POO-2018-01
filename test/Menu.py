import sys

class Menu:

   def __init__(self):
       self.break_while=1
       self.choices={
       "1":self.Administrador,
       "2":self.Usuario,
       "3":self.Invitado,
       "4":self.Salir
       }

   def Seleccionarop(self):
         pass

   def menuPrincipal(self):
      print("""
      Cheapy Menu Principal

         1. Administrador
         2. Usuario
         3. Invitado 
         4. Salir

      """)

   def Administrador(self):
      print("""
      CHEAPY Menu Administrador

         1. Ver usuarios
         2. Crear usuario
         3. Eliminar Usuario
         4. Crear playlist
         5. Eliminar playlist
         6. Crear albúm
         7. Eliminar albúm
         8. Crear artista
         9. Eliminar artista
         10. Agregar comentario
         11. Eliminar comentario
         12. Salir

         """)
      op = int(input("ingrese opcion: "))

      if (op==1):
         self.verUsuarios()
      elif(op==2):
         self.crearUsuario()
      elif(op==3):
         self.EliminarUsuario()
      elif(op==4):
         self.crearPlaylist()
      elif(op==5):
         self.eliminarPlaylist()
      elif(op==6):
         self.crearAlbum()
      elif(op==7):
         self.eliminarAlbum()
      elif(op==8):
         self.crearArtista()
      elif(op==9):
         self.eliminarArtista()
      elif(op==10):
         self.agregarComentario()
      elif(op==11):
         self.eliminarComentario()
      elif(op==12):
         pass

   def verUsuarios(self):
      print("\nfuncion funciona")
      self.Administrador()

   def crearUsuario(self):
      self.Administrador()

   def EliminarUsuario(self):
      self.Administrador()

   def crearPlaylist(self):
      self.Administrador()

   def eliminarPlaylist(self):
      self.Administrador()

   def crearAlbum(self):
      self.Administrador()

   def eliminarAlbum(self):
      self.Administrador()

   def crearArtista(self):
      self.Administrador()

   def eliminarArtista(self):
      self.Administrador()

   def agregarComentario(self):
      self.Administrador()

   def eliminarComentario(self):
      self.Administrador()

   def Usuario(self):
      print("""
      CHEAPY Menu Usuario
        1. Crear playlist
        2. Eliminar playlist
        3. Agrega comentario
        4. Eliminar comentario
        5. Salir
        
        """)

      op = int(input("ingrese opcion: "))

      if (op==1):
         self.crearPlaylist()
      elif(op==2):
         self.eliminarPlaylist()
      elif(op==3):
         self.agregarComentario()
      elif(op==4):
         self.eliminarComentario()
      elif(op==5):
         self.eliminarPlaylist()

   def Invitado(self):
      print("""
      CHEAPY Menu Usuario
        
        3.1. Registrase
        3.2. Ver playlist
        3.3. Salir

        """)

   def Registrase(self):
      self.Invitado()

   def verPlaylist(self):
      self.Invitado()

   def Salir(self):
      print("\nFin del programa")
      sys.exit(0)

   def run(self):
      while self.break_while==1:
         self.menuPrincipal()
         opcionMenu = input("ingresar una opcion: ")
         action = self.choices.get(opcionMenu)
         if action:
            action()
         else:
            print("{0} no es una opcion valida".format(opcion))

         
if __name__ == "__main__":
   Menu().run()
