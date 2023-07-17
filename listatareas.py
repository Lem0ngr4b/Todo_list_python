lista_de_tareas = []

def agregar_tarea(tarea):
    lista_de_tareas.append(tarea)
    print("tarea agregada exitosamente! :D")

def eliminar_tarea(tarea):
    if tarea in lista_de_tareas:
        lista_de_tareas.remove(tarea)
        print("tarea eliminada :c")
    else:
        print("tarea no existente :/")

def editar_tarea(tarea_vieja, tarea_nueva):
    if tarea_vieja in lista_de_tareas:
        indice = lista_de_tareas.index(tarea_vieja)
        lista_de_tareas[indice] = tarea_nueva
        print("Tarea editada con éxito.")
    else:
        print("La tarea no existe en la lista.")



def mostrar_tareas():
    if len(lista_de_tareas) > 0:
        print("lista de tareas")
        for tarea in lista_de_tareas:
            print("-", tarea)
    else:
        print("No hay tareas en la lista") 

print("Bienvenido a la lista de tareas!!")

# Bucle principal
while True:
    print("¿Qué acción deseas realizar?")
    print("1. Agregar tarea")
    print("2. Eliminar tarea")
    print("3. Editar tarea")
    print("4. Mostrar tareas")
    print("5. Salir")

    opcion = input("Ingrese el número de la opción: ")

    if opcion == "1":
        tarea = input("Ingrese la tarea que desea agregar: ")
        agregar_tarea(tarea)
    elif opcion == "2":
        tarea = input("Ingrese la tarea que desea eliminar: ")
        eliminar_tarea(tarea)
    elif opcion == "3":
         tarea_vieja = input("Ingrese tarea que desea editar: ")
         tarea_nueva = input("Ingrese nueva descripcion de la tarea: ")
         editar_tarea(tarea_vieja, tarea_nueva)
    elif opcion == "4":
        mostrar_tareas()
    elif opcion == "5":
        print("Saliendo del programa...")
        break
    else:
        print("Opción inválida. Por favor, ingrese un número válido.")



        



