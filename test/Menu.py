import sys

"""
from Admin import Admin
from Artista import Artista
from Cancion import Cancion
from Album import Album
from Comentarios import Comentarios
from Lista import Lista
from User import User 
"""

class Menu:

   def __init__(self):
       self.break_while=1
       self.choices={
       "1":self.administrador,
       "2":self.usuario,
       "3":self.invitado,
       "4":self.salir
       }

   def menuPrincipal(self):
      print("""
      Cheapy Menu Principal
         1. Administrador
         2. Usuario
         3. Invitado 
         4. Salir

      """)

   def administrador(self):
      break_while=True
      while(break_while) :
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
            self.eliminarUsuario()
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
            break_while = False

   def verUsuarios(self):
      print("\nfuncion funciona")
      
   def crearUsuario(self):
      pass

   def eliminarUsuario(self):
      pass

   def crearPlaylist(self):
      pass

   def eliminarPlaylist(self):
      pass

   def crearAlbum(self):
      pass

   def eliminarAlbum(self):
      pass
      
   def crearArtista(self):
      pass

   def eliminarArtista(self):
      pass

   def agregarComentario(self):
      pass

   def eliminarComentario(self):
      pass

   def usuario(self):
      break_while=True
      while(break_while):
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
            break_while=False

   def invitado(self):
      break_while=True
      while (break_while):
         print("""
         CHEAPY Menu Usuario
           1. Registrase
           2. Ver playlist
           3. Salir

           """)

         op = int(input("Ingrese opcion: "))
         if (op==1):
            self.registrase()
         elif(op==2):
            self.verPlaylist()
         elif(op==3):
            break_while=False

   def registrase(self):
      pass

   def verPlaylist(self):
      pass

   def salir(self):
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
