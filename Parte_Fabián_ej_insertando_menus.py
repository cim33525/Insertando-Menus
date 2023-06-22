import sys

continuacion = 0

dic_adm = {
    "num_adm": 1212577,
    "clave_adm": "jefeadm989",
}

dic_usuario_uno = {
    "num_uno": 38752321,
    "clave_uno": "natu55perez",
}

dic_usuario_dos = {
    "num_dos": 19205489,
    "clave_dos": "stelly22a",
}
                 
dic_usuario_tres = {
    "num_tres": 24021865,
    "clave_tres": "norber89g",
}   

dic_usuario_cuatro = {
    "num_cuatro": 35455322,
    "clave_cuatro": "wili96rs",
}  
        
dic_usuario_cinco = {
    "num_cinco": 14258367,
    "clave_cinco": "dto1jmg",
} 
        
dic_usuario_seis = {
    "num_seis": 9327586,
    "clave_seis": "niconico77",
}  

dic_usuario_siete = {
    "num_siete": 31319564,
    "clave_siete": "22jmarquez",
}    
        
dic_usuario_ocho = {
    "num_ocho": 20019213,
    "clave_ocho": "mascota1144",
}     
        
dic_usuario_nueve = {
    "num_nueve": 34817922,
    "clave_nueve": "edificiomar11",
}   

def seg_contrasenia_adm ():
    if num_caracteres_adm <= 3:
         print(f"Bienvenido administrador/a {administrador} al sistema de gestión del consorcio del edificio!!!")
         print(f"Le debemos informar que su contraseña posee {num_caracteres_adm} caracteres, lo que significa que es débil en términos de seguridad.")
    elif num_caracteres_adm >= 4 and num_caracteres_adm <= 7:
         print(f"Bienvenido administrador/a {administrador} al sistema de gestión del consorcio del edificio!!!")
         print(f"Le debemos informar que su contraseña posee {num_caracteres_adm} caracteres, lo que significa que es normal en términos de seguridad.")
    else:
         print(f"Bienvenido administrador/a {administrador} al sistema de gestión del consorcio del edificio!!!")
         print(f"Le debemos informar que su contraseña posee {num_caracteres_adm} caracteres, lo que significa que es fuerte en términos de seguridad.")

def mostrar_bienvenida_admin():
    mensaje = "********* 🔓 Bienvenido al modo Administrador 🔓 *********\nTe mostramos todo lo que podés hacer desde la app de tu consorcio, sin moverte de donde estés. Selecciona tu opción:\n"
    mensaje += "[1] Gestion de Usuarios\n"
    mensaje += "[2] Administrar Proveedores\n"
    mensaje += "[3] Obtener Reportes\n"
    mensaje += "[6] Salir del sistema\n"
    return mensaje

def seg_contrasenia_usuario ():
    if num_caracteres <= 3:
         print(f"Bienvenido usuario/a {usuario} al sistema de gestión del consorcio del edificio!!!")
         print(f"Le debemos informar que su contraseña posee {num_caracteres} caracteres, lo que significa que es débil en términos de seguridad.")
    elif num_caracteres >= 4 and num_caracteres <= 7:
         print(f"Bienvenido usuario/a {usuario} al sistema de gestión del consorcio del edificio!!!")
         print(f"Le debemos informar que su contraseña posee {num_caracteres} caracteres, lo que significa que es normal en términos de seguridad.")
    else:
         print(f"Bienvenido usuario/a {usuario} al sistema de gestión del consorcio del edificio!!!")
         print(f"Le debemos informar que su contraseña posee {num_caracteres} caracteres, lo que significa que es fuerte en términos de seguridad.")

acceso = input("Bienvenido al programa del consorcio, por favor ingrese 1 si usted es administrador o 2 si usted es un usuario: ")
while acceso != "1" and acceso != "2":
    acceso = input("Por favor introduzca una opción válida: ")

match acceso:
    case "1":
        print("Hola administrador, para continuar debe ingresar su número de identificación y contraseña: ")
        while continuacion < 3:
            while True:
                try:
                    administrador = int(input("Hola, ahora indicanos tu número de identificación: "))    
                except ValueError:
                    print("Se debe escribir un número para la identificación del administrador.")
                    continue
                else:
                    break
            contrasenia_adm = input("Ahora por favor tu contraseña: ")

            num_caracteres_adm = len(contrasenia_adm)

            if administrador in dic_adm.values() and contrasenia_adm in dic_adm.values():
                seg_contrasenia_adm ()
                mostrar_bienvenida_admin ()          # Acá debe ir el menu admin para el administrador; y todo el código relacionado con el administrador debe colocarse aquí, para que quede separado del código utilizado por los usuarios.
                sys.exit()                           # Éste sys.exit () con el código completo se va a ejecutar cuando el administrador seleccione la opción salir del sistema.
            else:
                print("Introdujo el número de identificación del administrador y/o contraseña incorrectos, intente de nuevo")
                continuacion += 1
        if continuacion == 3:
            print("La aplicación no permite ingresar más de 3 intentos, mañana podrá volver a intentarlo, gracias.")
            sys.exit()

    case "2":
        print("Hola usuario, por favor para acceder al programa debe ingresar su número de usuario y contraseña:")
        while continuacion < 3:
            while True:
                try:
                    usuario = int(input("Hola, ahora indicanos tu usuario: "))     # acá y en adelante quedó identificado el usuario (quedó guardado su número ingresado en la variable usuario)
                except ValueError:
                    print("Se debe escribir un número para el usuario.")
                    continue
                else:
                    break
            contrasenia = input("Ahora por favor tu contraseña: ")

            num_caracteres = len(contrasenia)

            if usuario in dic_usuario_uno.values() and contrasenia in dic_usuario_uno.values():
                seg_contrasenia_usuario()
                break
            elif usuario in dic_usuario_dos.values() and contrasenia in dic_usuario_dos.values():
                seg_contrasenia_usuario()
                break
            elif usuario in dic_usuario_tres.values() and contrasenia in dic_usuario_tres.values():
                seg_contrasenia_usuario()
                break
            elif usuario in dic_usuario_cuatro.values() and contrasenia in dic_usuario_cuatro.values():
                seg_contrasenia_usuario()
                break
            elif usuario in dic_usuario_cinco.values() and contrasenia in dic_usuario_cinco.values():
                seg_contrasenia_usuario()
                break
            elif usuario in dic_usuario_seis.values() and contrasenia in dic_usuario_seis.values():
                seg_contrasenia_usuario()
                break
            elif usuario in dic_usuario_siete.values() and contrasenia in dic_usuario_siete.values():
                seg_contrasenia_usuario()
                break
            elif usuario in dic_usuario_ocho.values() and contrasenia in dic_usuario_ocho.values():
                seg_contrasenia_usuario()
                break
            elif usuario in dic_usuario_nueve.values() and contrasenia in dic_usuario_nueve.values():
                seg_contrasenia_usuario()
                break
            else:
                print("Introdujo un usuario y/o contraseña incorrectos, intente de nuevo")
                continuacion += 1

        if continuacion == 3:
            print("La aplicación no permite ingresar más de 3 intentos, mañana podrá volver a intentarlo, gracias.")
            sys.exit()

# A partir de acá ponemos el menu Usuario, vean a continuación que se muestra siempre el usuario correcto:

print(f"""
            Bienvendo Sr/a {usuario}.
            Te mostramos todo lo que podés hacer desde la app de tu consorcio, sin moverte de donde estés.

                [1] Conocé más tu edificio
                [2] Datos de proveedores (lista de proveedores con teléfonos útiles / encargado horario laboral)
                [3]Últimas expensas 
                [4]Informá tu pago
                [5]Gestioná tu reclamo 
                [6] Salir del sistema
            """)
opcion_menu = int(input("Ingrese una opcion de acuerdo a lo requerido: "))