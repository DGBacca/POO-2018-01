import sys
from Admin import Admin
from Artista import Artista
from Cancion import Cancion
from Album import Album
from Comentarios import Comentarios
from Lista import Lista
from User import User

class Menu():

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
      CHEAPY Menu Principal
         1. Administrador
         2. Usuario
         3. Invitado 
         4. Salir

      """)
#### Menu del admisnitrador ######
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
            print("La cantidad de usarios registrados es: \n" ,
               User.CONTADOR_USERS)
         elif(op==2):
            User.registrar_usuario()
         elif(op==3):
            User.eliminarUsuario()
         elif(op==4):
            Lista.crearLista()
         elif(op==5):
            Lista.eliminarLista()
         elif(op==6):
            Album.rearAlbum()
         elif(op==7):
            Album.eliminarAlbum()
         elif(op==8):
            Artista.crearArtista()
         elif(op==9):
            Artista.eliminarArtista()
         elif(op==10):
            Comentarios.agregarComentario()
         elif(op==11):
            Comentarios.eliminarComentario()
         elif(op==12):
            break_while = False
   
##### Menu de usuario registrado ######
   def usuario(self):
      email = str(input("Ingrese E-mail: "))
      password = str(input("Ingrese contraseña: "))                 # Usuario se loguea             
      posible_User = None #User.autenticarUsuario(email,password)   # validacion de usuario logueado
      if(posible_User==None):
         print("Usuario no encontrado")
      else:
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
               Lista.crearLista()
            elif(op==2):
               Lista.eliminarLista()
            elif(op==3):
               Comentarios.agregarComentario()
            elif(op==4):
               comentarios.eliminarComentario()
            elif(op==5):
               break_while=False

##### Menu de usuario invitado ######
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
            User.registrar_usuario()
         elif(op==2):
            Lista.verlistas()
         elif(op==3):
            break_while=False

   def registrase(self):
      User.registrar_usuario()
      # verificar metodo guardar

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
