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
    ingreso = input("Ingrese la contraseña Empresarial dada por el administrador: ")
    if ingreso == Contraseña_Correcta:
        print(Fore.GREEN + "Contraseña correcta. Acceso concedido." + Style.RESET_ALL)
        break # Termina el ciclo al ingresar la contraseña correcta
    else:
        intentos -= 1
        print(Fore.RED + f"Contraseña incorrecta. Te quedan {intentos} intentos." + Style.RESET_ALL)
        if intentos == 0:
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

print("\n Bienvenido al sistema de control laboral \n")

while True:
    mostrar_menu()#Aqui se llama a la funcion que se creo anteriormente para mostrar el menu de registro de asistencia y puntualidad.
    opcion = input("Seleccione la opción que desea elegir: ")

    if opcion == "1":
        while True:
            nombre = input("Ingrese el nombre del empleado: ").strip().capitalize()
            documento = input("Ingrese el documento del empleado: ").strip()#Aqui se pide al usuario que ingrese el nombre y el documento del empleado y se utiliza .strip() para eliminar los espacios en blanco al inicio y al final de la cadena.
            cargo = input("Ingrese el cargo del empleado: ").strip().capitalize()
 #Aqui se hace un proceso para que verifique si el empleado ingresado ya existe en la lista de empleados.
            existe = False
            for emp in empleados:
                if emp[0] == nombre and emp[1] == documento:
                    existe = True
                    break

            if not existe:#Si el empleado no existe, se agrega a la lista de empleados.
                empleados.append((nombre, documento, cargo))
                print(Fore.GREEN + f"Empleado {nombre} registrado correctamente." + Style.RESET_ALL)
            else:
                print(Fore.YELLOW + f"El empleado {nombre} ya está registrado." + Style.RESET_ALL)

            while True:
                fecha = input("Ingrese la fecha de ingreso (DD/MM/AAAA): ").strip()
                hora = input("Ingrese la hora de ingreso del trabajador (HH:MM) (En caso de no haber asistido deje el espacio vacio y ingrese la tecla enter) ): ").strip()

                ya_existe = any(r['nombre'] == nombre and r['fecha'] == fecha for r in asistencias)
                if ya_existe:#Aqui se verifica si ya existe un registro de asistencia para el trabajador en la fecha ingresada.
                    print(Fore.YELLOW + "⚠ Ya existe un registro de asistencia para este trabajador en esa fecha." + Style.RESET_ALL)
                    seguir = input("¿Desea registrar otra fecha? [SI] / [NO]: ").strip().upper()
                    if seguir != "SI":
                        break
                    else:
                        continue#Si ya existe un registro, se utiliza continue para volver al inicio del ciclo y pedir al usuario que ingrese los datos nuevamente.
                #guardar el registro
                if hora == "":
                    estado = "AUSENTE" #Aqui se verifica si la hora ingresada esta vacia, si es asi se clasifica el estado como "NO LLEGO".
                elif hora <= "08:00":
                    estado = "PUNTUAL"#Si la hora ingresada es menor o igual a las 08:00, se clasifica el estado como "PUNTUAL".
                else:
                    estado = "TARDE"

                asistencias.append({
                    "nombre": nombre,
                    "documento": documento,  # <-- agrega esto
                    "hora": hora if hora else "No llegó",
                    "fecha": fecha,
                    "estado": estado
                })

                print(Fore.CYAN + f"\n✅ Registro guardado para {nombre} – {estado} ({fecha})" + Style.RESET_ALL)

                repetir = input("¿Desea registrar otra fecha para este mismo trabajador? [SI] / [NO]: ").strip().upper()
                if repetir != "SI":
                    break #Aqui se rompe el ciclo de ingresar fechas para el mismo trabajador

            otro = input("¿Desea registrar otro trabajador diferente? [SI] / [NO]: ").strip().upper()
            if otro != "SI":
                print("Volviendo al menú principal...\n")
                break
  # Opción 2: Ver historial de asistencia
    elif opcion == "2":
        print("\n  Historial de asistencia:")
        if len(asistencias) == 0:
            print("No hay registros todavía.")
        else:
            for registro in asistencias:
                print(f"{registro['nombre']} / {registro['documento']} / {registro['hora']} / {registro['fecha']} → LLEGÓ {registro['estado']}")

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
                    total += 1
                    if r['estado'] == "PUNTUAL":
                        puntuales += 1

            if total > 0:
                porcentaje = round((puntuales / total) * 100, 2)
                print(f" El trabajador {nombre_buscado} obtuvo un porcentaje de puntualidad de {porcentaje}%")
            else:
                print(f" No se encontraron registros para {nombre_buscado}.")

            seguir = input("¿Desea saber el porcentaje de otro trabajador? [SI] / [NO]: ").upper()
            if seguir != "SI":
                break
    # Opción 4: Generar informe semanal
    elif opcion == "4":
        print("\n Informe semanal de puntualidad:")
        resumen = {}
        for r in asistencias:
            nombre = r["nombre"]
            if nombre not in resumen:
                resumen[nombre] = {"total": 0, "puntuales": 0}
            resumen[nombre]["total"] += 1
            if r["estado"] == "PUNTUAL":
                resumen[nombre]["puntuales"] += 1

        if not resumen:
            print("No hay registros de asistencia para generar el informe.")
        else:
            for nombre, datos in resumen.items():
                porcentaje = round((datos["puntuales"] / datos["total"]) * 100, 2)
                print(f"- {nombre} obtuvo un {porcentaje}% de cumplimiento")

        volver = input("\n¿Desea volver al menú? [SI] / [NO]: ").upper()
        if volver != "SI":
            print("Saliendo del programa.")
            break

    elif opcion == "5":
        print("\n Lista de empleados registrados:")
        if not empleados:
            print("No hay empleados registrados aún.")
        else:
            for i, emp in enumerate(empleados, 1):
                print(f"{i}. Nombre: {emp[0]}, Documento: {emp[1]}, Cargo: {emp[2]}")
        input("\nPresione Enter para volver al menú...")

    elif opcion == "6":
        print("\n Saliendo del menú. ¡Hasta luego!")
        break

    else:
        print("Opción inválida. Intente nuevamente.")