from colorama import init, Fore, Style
init()

asistencias = []  #Se crea una lista vacia para almacenar los registros de asistencia y puntualidad de los trabajadores.
empleados = []

# Título
titulo = "GRUPO EMPRESARIAL PROACTIVA S.A.S Registro De Asistencia y Puntualidad"
print("\n" + Fore.CYAN + "=" * 80)  # Aquí se agrega el color cyan para que se vea más llamativo el título a la hora de modificarlo.
print(titulo.center(80))
print("=" * 80 + Style.RESET_ALL + "\n") # Aqui se imprime una line de 80 caracteres para que a la hora de codificar se codifique centrado y tenga una buena estructura.

# Acceso
#Acontinuación se empezara creando una contraseña para que la empresa pueda acceder a la pagina de registro de asistencia y puntualidad
subtitulo = "ACCESO SEGURO A LA EMPRESA"
print("\n" + "=" * 50)
print(subtitulo.center(50))#Se crea un tipo subtitulo para abrir el paso y notificar al lector que esta en la parte de acceso a la empresa
print("=" * 50 + "\n")

Contraseña_Correcta = "S.A.S2025"#Se crea una contraseña y una variable con el numero de intentos que se le da al usuario para ingresar la contraseña correcta.
intentos = 3#Se crea una contraseña y una variable con el numero de intentos que se le da al usuario para ingresar la contraseña correcta.

while intentos > 0:
    ingreso = input("Ingrese la contraseña Empresarial dada por el administrador: ") #Aca se pide al usuario que ingrese la contraseña para poder acceder al sistema de registro de asistencia y puntualidad.
    if ingreso == Contraseña_Correcta: #si la contraseña es igual de ingreso es igual a la contraseña correcta, se le da acceso al usuario.
        print(Fore.GREEN + "Contraseña correcta. Acceso concedido." + Style.RESET_ALL)
        break # Termina el ciclo al ingresar la contraseña correcta
    else:
        intentos -= 1 #Si la contraseña ingresada es incorrecta, se le resta un intento al usuario y se le informa cuántos intentos le quedan.
        print(Fore.RED + f"Contraseña incorrecta. Te quedan {intentos} intentos." + Style.RESET_ALL) #Se imprime el mensaje de que la contraseña es incorrecta y cuántos intentos le quedan al usuario
        if intentos == 0: #Si el usuario se queda sin intentos, se le informa que ha agotado todos los intentos y se le sugiere consultar al administrador.
            print(Fore.RED + "Has agotado todos los intentos. Acceso denegado. Consulta al administrador." + Style.RESET_ALL)
            exit()#Termina el ciclo al usuario fallar los tres intentos

def mostrar_menu():#Aqui se crea una funcion para mostrar el menu de registro de asistencia y puntualidad y se utiliza def (define-definicion) para reutilizar el codigo sin ingresarlo varias veces.
    print("\n" + "=" * 60)
    print("MENU DE REGISTRO DE ASISTENCIA Y PUNTUALIDAD".center(60))
    print("=" * 60)
    print("1. Registrar asistencia")
    print("2. Ver historial  de asistencia")
    print("3. Calcular porcentaje de puntualidad por empleado")
    print("4. Generar informe semanal")
    print("5. Ver empleados registrados")
    print("6. Salir del menú")
    print("=" * 60)

print("\n Bienvenido al sistema de control laboral \n") #Se imprime un mensaje de bienvenida al sistema de control labora y se usa \n para que se imprima en una nueva linea.

while True: #Se crea un ciclo infinito para que el usuario pueda interactuar con el menu de registro de asistencia y puntualidad.
    mostrar_menu()#Aqui se llama a la funcion que se creo anteriormente para mostrar el menu de registro de asistencia y puntualidad.
    opcion = input("Seleccione la opción que desea elegir: ")

    if opcion == "1":
        while True: #while true es un ciclo que se ejecuta indefinidamente hasta que se rompa con un break. 
            #a difeencia de el while normal que se ejecuta mientras la condicion sea verdadera, el while true se ejecuta indefinidamente hasta que se rompa con un break.
            nombre = input("Ingrese el nombre del empleado: ").strip().capitalize()
            documento = input("Ingrese el documento del empleado: ").strip()#Aqui se pide al usuario que ingrese el nombre y el documento del empleado y se utiliza .strip() para eliminar los espacios en blanco al inicio y al final de la cadena.
            cargo = input("Ingrese el cargo del empleado: ").strip().capitalize() #Se pide al usuario que ingrese el cargo del empleado y se utiliza .capitalize() para que la primera letra de cada palabra sea mayúscula.
 #Aqui se hace un proceso para que verifique si el empleado ingresado ya existe en la lista de empleados.
            existe = False #Se crea una variable booleana llamada existe y se inicializa en False para verificar si el empleado ya existe en la lista de empleados.
            for emp in empleados: #Se crea un ciclo for para recorrer la lista de empleados y verificar si el empleado ya existe y se usa emp para representar cada empleado en la lista.
                if emp[0] == nombre and emp[1] == documento: #Se verifica si el nombre y el documento del empleado ya existen en la lista de empleados.
                    existe = True 
                    break #Si el empleado ya existe, se cambia el valor de la variable existe a True y se rompe el ciclo for.

            if not existe:#Si el empleado no existe, se agrega a la lista de empleados.
                empleados.append((nombre, documento, cargo)) #Se agrega el empleado a la lista de empleados como una tupla con el nombre, documento y cargo del empleado.
                print(Fore.GREEN + f"Empleado {nombre} registrado correctamente." + Style.RESET_ALL)
            else:
                print(Fore.YELLOW + f"El empleado {nombre} ya está registrado." + Style.RESET_ALL) #se sigue usando el color amarillo para que se vea más llamativo el mensaje de que el empleado ya esta registrado.

            while True: #Se crea un ciclo while true para que el usuario pueda ingresar varias fechas de asistencia para el mismo trabajador.
                fecha = input("Ingrese la fecha de ingreso (DD/MM/AAAA): ").strip() #Se pide al usuario que ingrese la fecha de ingreso del trabajador y se utiliza .strip() para eliminar los espacios en blanco al inicio y al final de la cadena.
                hora = input("Ingrese la hora de ingreso del trabajador (HH:MM) (En caso de no haber asistido deje el espacio vacio y ingrese la tecla enter) ): ").strip() #Se pide al usuario que ingrese la hora de ingreso del trabajador y se utiliza .strip() para eliminar los espacios en blanco al inicio y al final de la cadena.

                ya_existe = any(r['nombre'] == nombre and r['fecha'] == fecha for r in asistencias) #Se utiliza la función any() para verificar si ya existe un registro de asistencia para el trabajador en la fecha ingresada. y el r para recorrer la lista de asistencias.
                if ya_existe:#Aqui se verifica si ya existe un registro de asistencia para el trabajador en la fecha ingresada.
                    print(Fore.YELLOW + " Ya existe un registro de asistencia para este trabajador en esa fecha." + Style.RESET_ALL)
                    seguir = input("¿Desea registrar otra fecha? [SI] / [NO]: ").strip().upper()
                    if seguir != "SI": #Si el usuario no desea registrar otra fecha, se rompe el ciclo y se vuelve al inicio del ciclo principal.
                        break
                    else:
                        continue#Si ya existe un registro, se utiliza continue para volver al inicio del ciclo y pedir al usuario que ingrese los datos nuevamente.
                #guardar el registro
                if hora == "":
                    estado = "AUSENTE" #Aqui se verifica si la hora ingresada esta vacia, si es asi se clasifica el estado como "NO LLEGO".
                elif hora <= "08:00":
                    estado = "PUNTUAL"#Si la hora ingresada es menor o igual a las 08:00, se clasifica el estado como "PUNTUAL".
                else:
                    estado = "TARDE" #Si la hora ingresada es mayor a las 08:00, se clasifica el estado como "TARDE".
                #Aqui se agrega el registro de asistencia a la lista de asistencias.

                asistencias.append({ #Se agrega un diccionario con los datos del registro de asistencia.
                    "nombre": nombre,
                    "documento": documento,  # <-- agrega esto
                    "hora": hora if hora else "No llegó",
                    "fecha": fecha,
                    "estado": estado
                })

                print(Fore.CYAN + f"\n Registro guardado para {nombre}  {estado} ({fecha})" + Style.RESET_ALL) #Se imprime un mensaje de que el registro se guardo correctamente y se utiliza el color cyan para que se vea más llamativo el mensaje.
                #Aqui se pregunta al usuario si desea registrar otra fecha para el mismo trabajador.

                repetir = input("¿Desea registrar otra fecha para este mismo trabajador? [SI] / [NO]: ").strip().upper() #Se pide al usuario que ingrese si desea registrar otra fecha para el mismo trabajador y se utiliza .strip() para eliminar los espacios en blanco al inicio y al final de la cadena.
                if repetir != "SI":
                    break #Aqui se rompe el ciclo de ingresar fechas para el mismo trabajador

            otro = input("¿Desea registrar otro trabajador diferente? [SI] / [NO]: ").strip().upper() #Se pregunta al usuario si desea registrar otro trabajador diferente y se utiliza .strip() para eliminar los espacios en blanco al inicio y al final de la cadena.
            if otro != "SI":
                print("Volviendo al menú principal...\n")
                break
  # Opción 2: Ver historial de asistencia
    elif opcion == "2":
        print("\n  Historial de asistencia:") #Se imprime un mensaje de que se esta viendo el historial de asistencia y se utiliza \n para que se imprima en una nueva linea.
        if len(asistencias) == 0: #Se verifica si la lista de asistencias esta vacia, si es asi se imprime un mensaje de que no hay registros.
            print("No hay registros todavía.")
        else:
            for registro in asistencias: #Se recorre la lista de asistencias y se imprime cada registro de asistencia.
                print(f"{registro['nombre']} / {registro['documento']} / {registro['hora']} / {registro['fecha']} → LLEGÓ {registro['estado']}") #Se imprime el nombre, el documento, la hora, la fecha y el estado del registro de asistencia.

        volver = input("\n¿Desea volver al menú? [SI] / [NO]: ").upper()
        if volver != "SI":
            print("Saliendo del programa.")
            break
  # Opción 3: Calcular porcentaje de puntualidad por empleado
    elif opcion == "3":
        while True:
            nombre_buscado = input("Ingrese el trabajador del cual desea saber el porcentaje de puntualidad: ").capitalize()
            total = 0 #Total de registros del empleado
            puntuales = 0 #veces que fue puntual

            for r in asistencias:
                if r['nombre'] == nombre_buscado:
                    total += 1 #Total de registros del empleado y el +1 se utiliza para contar la cantidad de veces que fue puntual
                    if r['estado'] == "PUNTUAL": #Si el estado es puntual
                        puntuales += 1 #veces que fue puntual

            if total > 0: #Si el total de registros es mayor a 0, se calcula el porcentaje de puntualidad
                porcentaje = round((puntuales / total) * 100, 2) #Se redondea el porcentaje a 2 decimales
                print(f" El trabajador {nombre_buscado} obtuvo un porcentaje de puntualidad de {porcentaje}%") #Se imprime el porcentaje de puntualidad del trabajador
            else:
                print(f" No se encontraron registros para {nombre_buscado}.") #Si no se encontraron registros para el trabajador, se imprime un mensaje indicando que no se encontraron registros.

            seguir = input("¿Desea saber el porcentaje de otro trabajador? [SI] / [NO]: ").upper()
            if seguir != "SI":
                break
    # Opción 4: Generar informe semanal
    elif opcion == "4": #Aqui se genera el informe semanal
        print("\n Informe semanal de puntualidad:")
        resumen = {} #Se crea un diccionario vacio llamado resumen para almacenar el total de registros y la cantidad de veces que fue puntual por cada trabajador.
        for r in asistencias: #Se recorre la lista de asistencias y se crea un diccionario resumen que almacena el total de registros y la cantidad de veces que fue puntual por cada trabajador.
            nombre = r["nombre"] #Se obtiene el nombre del trabajador del registro de asistencia.
            if nombre not in resumen: #Si el nombre del trabajador no esta en el diccionario resumen, se agrega con un total de 0 registros y 0 veces que fue puntual.
                resumen[nombre] = {"total": 0, "puntuales": 0} #Aqui se crea un diccionario llamado resumen que almacena el total de registros y la cantidad de veces que fue puntual por cada trabajador.
            resumen[nombre]["total"] += 1 #Aqui se crea un diccionario llamado resumen que almacena el total de registros y la cantidad de veces que fue puntual por cada trabajador.
            if r["estado"] == "PUNTUAL": #Si el estado es puntual, se suma 1 al total de registros del empleado y a la cantidad de veces que fue puntual.
                resumen[nombre]["puntuales"] += 1 #Aqui se crea un diccionario llamado resumen que almacena el total de registros y la cantidad de veces que fue puntual por cada trabajador.

        if not resumen:
            print("No hay registros de asistencia para generar el informe.") #Si el diccionario resumen esta vacio, se imprime un mensaje indicando que no hay registros de asistencia para generar el informe.
        else:
            for nombre, datos in resumen.items(): #Se recorre el diccionario resumen y se imprime el nombre del trabajador, el total de registros y la cantidad de veces que fue puntual.
                porcentaje = round((datos["puntuales"] / datos["total"]) * 100, 2) #Se calcula el porcentaje de puntualidad del trabajador y se redondea a 2 decimales.
                print(f"- {nombre} obtuvo un {porcentaje}% de cumplimiento") #Se imprime el nombre del trabajador y el porcentaje de puntualidad.

        volver = input("\n¿Desea volver al menú? [SI] / [NO]: ").upper()
        if volver != "SI":
            print("Saliendo del programa.")
            break

    elif opcion == "5":
        print("\n Lista de empleados registrados:") #Se imprime un mensaje de que se esta viendo la lista de empleados registrados y se utiliza \n para que se imprima en una nueva linea.
        if not empleados: #Se verifica si la lista de empleados esta vacia, si es asi se imprime un mensaje de que no hay empleados registrados.
            print("No hay empleados registrados aún.")
        else:
            for i, emp in enumerate(empleados, 1): #Se recorre la lista de empleados y se imprime el nombre, el documento y el cargo de cada empleado.
                print(f"{i}. Nombre: {emp[0]}, Documento: {emp[1]}, Cargo: {emp[2]}") #Se utiliza enumerate para numerar los empleados desde 1.
        input("\nPresione Enter para volver al menú...") #Se pide al usuario que presione Enter para volver al menú.

    elif opcion == "6":
        print("\n Saliendo del menú. ¡Hasta luego!")
        break

    else:
        print("Opción inválida. Intente nuevamente.")