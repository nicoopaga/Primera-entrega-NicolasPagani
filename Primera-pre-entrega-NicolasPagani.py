import json

# Diccionario para almacenar las credenciales de usuario
credentials = {}

#Contador para intentos de inicio de sesion fallidos
intentos_fallidos = {}

#Funcion para guardar las credenciales en un archivo de texto
def guardar_datos():
    with open("datos.txt", "w") as archivo: #Se utiliza w porque se realiza escritura. 
        json.dump(credentials, archivo)

#Funcion para registrarse
def register():
    while True: 
        username = input("Ingresa un nuevo nombre de usuario: ")
        if username in credentials:
            print("El nombre de usuario ya existe. Porfavor elija otro nombre de usuario.")
        else: 
            password = input("Ingrese una contraseña: ")
            credentials[username] = password
            print("Registro exitoso.")
            guardar_datos()
            break

#Funcion para iniciar sesion
def login():
        username = input("Ingrese su nombre de usuario: ")
        while True: #Esta funcionalidad verifica que si usuario es correcto, solo solicite reingresar la contraseña
            if username not in credentials:
                print("El nombre de usuario no existe. Porfavor registrese.")
                register()
            else:
                password = input("Ingrese su contraseña: ")
                if credentials.get(username) == password:
                    intentos_fallidos[username] = 0
                    print("Inicio de sesión exitoso.")
                    break
                else:
                    intentos_fallidos[username] = intentos_fallidos.get(username, 0) + 1
                    print("Contraseña incorrecta. Intente nuevamente.")
                    if intentos_fallidos.get(username, 0) == 3:
                        print("Tres intentos fallidos. Porfavor, cambie la contraseña.")
                        register()
                        break


#Funcion para realizar cambio de contraseña 
def change_password():
    username = input("Ingrese su nombre de usuario: ")
    if username in credentials:
        new_password = input("Ingrese su nueva contraseña: ")
        if new_password == credentials[username]:
            print("La nueva contraseña no puede ser igual a la anterior. Por favor, pruebe otra.")
        else:
            credentials[username] = new_password
            print("Contraseña cambiada exitosamente.")
            guardar_datos()  # Guardar después de cambiar la contraseña
    else:
        print("Nombre de usuario no encontrado. No se puede cambiar la contraseña.")

#Funcion para cargar las credenciales desde el archivo 
def cargar_datos():
    try: 
        with open("datos.txt", "r") as archivo: #Se utiliza r porque lee datos 
            data = json.load(archivo)
            credentials.update(data)
    except FileNotFoundError:
        # Si el archivo no existe, se ignora y se sigue adelante
        pass

#Main - La idea es colocar interactividad con el usuario. 
if __name__ == "__main__":
    cargar_datos() 
    while True: 
        print("\nBienvenido al prototipo de inicio de sesión.")
        print("1. Registrarse")
        print("2. Iniciar sesión")
        print("3. Cambiar contraseña")
        print("4. Salir")
        
        choice = input("Ingrese el número de opción que desea: ")
        
        if choice == "1":
            register()
        elif choice == "2":
            login()
        elif choice == "3":
            change_password()
        elif choice == "4":
            print("Hasta luego.")
            break
        else:
            print("Opción inválida. Intente nuevamente.")
