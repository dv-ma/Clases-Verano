numero1 = 0 #variable 1 declarada - es de tipo numérico
operacion = ''  #variable de tipo "string"
numero2 = 0 #segundo valor
resultado = 0 #ultima variable a utilizar en este caso. En la cabecera generalmente se declaran las variables a utilizar para mantener un orden y para optimizar
print("==CALCULADORA==")
print("Inserte primer número:") #para tener donde insertar el primer valor, primero hay que declarar una variable (primera linea)
numero1 = float(input()) #se le esta diciendo que almacene algo, en este caso un input. Para delimitar el tipo de dato a guardar, en este caso delimitarlo a numerico
print("Ingrese operación:")
operacion = input()
print("Ingrese segundo número:")
numero2 = float(input())


#if operacion == '+': # == para comparar, = asignar
#    resultado = numero1 + numero2
#    print(resultado)
#elif operacion == '-':

#    resultado = numero1 - numero2
#    print(resultado)                        #Se puede optimizar dejando el print al final sin tabular1
#elif operacion == '*':
#    resultado = numero1 * numero2
#    print(resultado)
#elif operacion == '/':
#    resultado = numero1 / numero2
#    print(resultado)

#case sirve para cuando hay muchas opciones, mientras que if y elif sirve mas para cuando son una cantidad pequeña de posibilidades

match operacion: #aqui se pone la variable correspondiente, en java generalmente se llame switch, y en base de datos generalmente tambien se llama case
    case '+':
        resultado = numero1 + numero2
    case '-':
        resultado = numero1 - numero2
    case '*':
        resultado = numero1 * numero2
    case '/':
        resultado = numero1 / numero2
    case _: #con guion bajo se indica que haga la operacion por defecto, es decir, en caso de que el usuario no haya una opcion, este entrega una por defecto
        print("Ingrese operacion valida")
print(resultado)
