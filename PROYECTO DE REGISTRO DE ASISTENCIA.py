from colorama import init, Fore , Style 
init()
asistencias = [] #Se crea una lista vacia para almacenar los registros de asistencia y puntualidad de los trabajadores.
titulo = "GRUPO EMPRESARIAL PROACTTIVO S.A.S Registro De Asistencia y Puntualidad"
print("\n" + Fore.CYAN + "=" * 80) #Aqui se agrega el color cyan para que s evea mas llamativo el titulo a la hora de modificarlo.
print(titulo.center(80))
print("=" * 80 + Style.RESET_ALL+"\n") # Aqui se imprime una line de 80 caracteres para que a la hora de codificar se codifique centrado y tenga una buena estructura.

#A continucacion se empezara creando una contraseña para que la empresa pueda acceder a la pagina de registro de asistencia y puntualidad.
import getpass
subtitulo= "ACCESO SEGURO A LA EMPRESA"
print("\n" + "=" * 50)
print(subtitulo.center(50))
print("=" * 50 + "\n") #Se crea un tipo subtitulo para abrir el paso y notificar al lector que esta en la parte de acceso a la empresa
Contraseña_Correcta = "S.A.S2025"
intentos=3 #Se crea una contraseña y una variable con el numero de intentos que se le da al usuario para ingresar la contraseña correcta.
while intentos > 0:
    ingreso = input ("Ingrese la contraseña Empresarial dada por el administrador: ")
    if ingreso == Contraseña_Correcta:
        print(Fore.GREEN + "Contraseña correcta. Acceso concedido." + Style.RESET_ALL)
        break #Aqui se detendria el ciclo al ingresar la contraseña correcta 
    else:
        intentos -= 1
        print(Fore.RED + f"Contraseña incorrecta. Te quedan {intentos} intentos." + Style.RESET_ALL)
        if intentos == 0:
            print(Fore.RED + "Has agotado todos los intentos. Acceso denegado Preguntale al administrador para desbloquear el acceso." + Style.RESET_ALL)
            exit()#Termina el ciclo al usuario fallar los tres intentos 
def mostrar_menu(): #Aqui se crea una funcion para mostrar el menu de registro de asistencia y puntualidady se utiliza def (define-definicion) para reutilizar el codigo sin ingresarlo varias veces.
    print("\n" + "=" * 60)
    print("MENU DE REGISTRO DE ASISTENCIA Y PUNTUALIDAD".center(60))
    print("=" * 60)
    print("1. Registrar asistencia")
    print("2. Ver historial  de asistencia")
    print("3. Calcular porcentaje de puntualidad por empleado")
    print("4. generar informe semanal")
    print("5. salir del menu ")
    print("=" * 60)
        
print("\n Bienvenido al sistema de control laboral \n")

while True:
    mostrar_menu()#Aqui se llama a la funcion que se creo anteriormente para mostrar el menu de registro de asistencia y puntualidad.
    opcion = input("Seleccione la opcion que desea elegir: ")
    if opcion == "1":
        nombre =input("ingrese el nombre del empleado: ").strip()
        while nombre:
            print("A continuacion este es el nombre que ingreso" , nombre)
            if nombre ==
                hora = input("Ingrese en la que el trabajador ingreso (HH:MM): ")
                fecha = input("Ingrese la fecha de ingreso (DD/MM/AAAA): ")
                estado = input("Ingrese el trabajador llego puntual,tarde o no llego): ").upper()
                #guardar el registro
                asistencias.append({
                    "nombre": nombre.capitalize(),
                    "hora": hora,
                    "fecha": fecha,
                    "estado": estado
                })
                otro = input("¿Desea registrar la asistencia de otro trabajador? [SI] [NO]: ").strip().upper() #Aqui se pide al usuario si desea registrar la asistencia de otro trabajador y se utiliza strip para eliminar los espacios en blanco y upper para convertir la respuesta en mayuscula.
                if otro != "SI":
                    print("A continuacion se  devolvera al menu de registro de asistencia ypuntualidad")
                    continue #Aqui se utiliza continue para volver al menu de registro de asistencia y puntualidad
                elif otro == "NO":
                    print("Volviendo al menun principal...")
                    break #Aqui se utiliza break para salir del ciclo y volver al menu principal
            # Opción 2: Ver historial de asistencia
    elif opcion == "2":
        print("\n  Historial de asistencia:")
        if len(asistencias) == 0:
            print("No hay registros todavía.")
        else:
            for registro in asistencias:
                print(f"{registro['nombre']} / {registro['hora']} / {registro['fecha']} → LLEGÓ {registro['estado']}")

        volver = input("\n¿Desea volver al menú? [SI] / [NO]: ").upper()
        if volver != "SI":
            print(" Saliendo del programa.")
            break

    # Opción 3: Calcular porcentaje de puntualidad por empleado
    elif opcion == "3":
        while True:
            trabajador = input("Ingrese el trabajador del cual desea saber el porcentaje de puntualidad: ").capitalize()
            total = 0
            puntuales = 0

            for r in asistencias:
                if r['nombre'] == trabajador:
                    total += 1
                    if r['estado'] == "PUNTUAL":
                        puntuales += 1

            if total > 0:
                porcentaje = round((puntuales / total) * 100, 2)
                print(f" El trabajador {trabajador} obtuvo un porcentaje de puntualidad de {porcentaje}%")
            else:
                print(f" No se encontraron registros para {trabajador}.")

            seguir = input("¿Desea saber el porcentaje de otro trabajador? [SI] / [NO]: ").upper()
            if seguir != "SI":
                break

    # Opción 4: Generar informe semanal
    elif opcion == "4":
        print("\n Informe semanal de puntualidad:")
        empleados = {}

        for r in asistencias:
            nombre = r["nombre"]
            if nombre not in empleados:
                empleados[nombre] = {"total": 0, "puntuales": 0}
            empleados[nombre]["total"] += 1
            if r["estado"] == "PUNTUAL":
                empleados[nombre]["puntuales"] += 1

        for nombre, datos in empleados.items():
            porcentaje = round((datos["puntuales"] / datos["total"]) * 100, 2)
            print(f"- {nombre} obtuvo un {porcentaje}% de cumplimiento")

        volver = input("\n¿Desea volver al menú? [SI] / [NO]: ").upper()
        if volver != "SI":
            print(" Saliendo del programa.")
            break

    # Opción 5: Salir
    elif opcion == "5":
        print("\n Saliendo del menú. ¡Hasta luego!")
        break

    else:
        print(" Opción inválida. Intente nuevamente.")