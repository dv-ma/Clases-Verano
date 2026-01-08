#Variables
opcion = 1
vuelo = 0
nombre = ""
apellido = ""
# for x in range (1,10):
#     for y in range (1,10):
#         print(x, 'x', y, '=', x*y)

while opcion != 0:
    print("==RESERVA DE VUELOS==")
    print("1) Listar")
    print("2) Reservar")
    print("3) Modificar")
    print("4) Eliminar")
    print("0) Salir")
    print("Ingrese opcion")
    opcion = int(input())
    
    match opcion:
        case 1:
            print("==Vuelos Disponibles==")
            print("1) Santiago - Brasil")
            print("2) Santiago - Argentina")
            print("3) Santiago - Canadá")
            print("4) ==Volver==")
            if opcion == 4
            return opcion 
            
        case 2:
            print("==Reservar==")
            print("1) Santiago - Brasil")
            print("2) Santiago - Argentina")
            print("3) Santiago - Canadá")
            print("Seleccione vuelo a reservar")
            #Agregar variable para reservar
            #Agregar nombre de pasajero
            reserva = int(input())
            if reserva == 1:
                print("Ingrese su nombre:")
                nombre = input()
                print("Ingrese su apellido:")
                apellido =  input()
                print(f"Su viaje Santiago - Brasil ha sido reservado exitosamente a nombre de {nombre, apellido}")
            
        case 3:
            print("==Modificar==")
            print("1) Santiago - Brasil")
            print("2) Santiago - Argentina")
            print("3) Santiago - Canadá")
            print("Ingrese vuelo a modificar")

        case 4:
            print("==Eliminar==")
            #Dejar la variable en 0
        case 0:
            print("¡Adiós!")
            #Mensaje de adiós personalizado
        case _:
            print("Ingrese una opción válida")