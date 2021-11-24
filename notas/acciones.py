import notas.nota as modelo
class Acciones:

    def crear(self,usuario):
        print(f"Ok {usuario[1]} vamos a crear una nueva nota!!")
        titulo=input("\nIntroduce el titulo de tu nota: ")
        descripcion=input("\n Mete el contenido de tu nota: ")
        nota=modelo.Nota(usuario[0],titulo,descripcion)
        guardar=nota.guardar()

        if guardar[0]>=1:
            print(f"\nPerfecto haz guardado la nota {nota.titulo}")
        else:
            print(f"No se ha guardado la nota {usuario[1]}, lo siento!!")

    def mostrar(self,usuario):
        print(f"Vale {usuario[1]} aquí tienes tus notas \n")
        nota=modelo.Nota(usuario[0])
        notas=nota.listar()

        for i in notas:
            print("------------------------------------")
            print(f"Titulo: {i[2]}")
            print(f"Descripcion: {i[3]}")
            print("------------------------------------\n")
    
    def borrar(self,usuario):
        print(f"Okey {usuario[1]} vamos a borrar notas")
        titulo=input("Introduce el titulo de la nota a borrar: ")

        nota=modelo.Nota(usuario[0],titulo)
        eliminar=nota.eliminar()
        
        if eliminar[0]>=1:
            print(f"Hemos borrado la nota: {nota.titulo}")
        else:
            print("No se ha borrado la nota prueba luego")