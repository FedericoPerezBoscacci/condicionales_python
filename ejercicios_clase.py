#!/usr/bin/env python
'''
Condicionales [Python]
Ejercicios de clase
---------------------------
Autor: Inove Coding School
Version: 1.1
 
Descripcion:
Programa creado para poner a prueba los conocimientos adquiridos durante la clase
'''

__author__ = "Inove Coding School"
__email__ = "alumnos@inove.com.ar"
__version__ = "1.1"

def ej1():
    # Ejercicios de práctica numérica
    
    # Comparadores
    # Ingrese dos números cualesquiera y realice las sigueintes
    # comparaciones entre ellos
    numero_1 = int(input('Ingrese el primer número:\n'))

    numero_2 = int(input('Ingrese el segundo número:\n'))
    


    # Compare cual de los dos números es mayor
    if numero_1 > numero_2:
        print("El primer numero ingresado es el mayor")
    else:
        print("El segundo numero ingresado es el mayor")

    

    # Imprima en pantalla según corresponda

    # Verifique si el numero_1 positivo, negativo o cero
    # Imprima el resultado en cada caso

    if numero_1 > 0:
        print("El primer numero ingresado es positivo")
    elif numero_1 <0:
        print("El primer numero ingresado es negativo")
    else:
        print("El primer numero ingresado es cero")
    
    # Verifique si el numero_1 es mayor a 0 y menor a 100
    # Imprima en pantalla si se cumple o no la condición

    if numero_1 > 0 and numero_1 < 100:
        print("El primer numero ingresado esta en el rango de 1 y 99")

    # Verifique si el numero_1 es menor a 10 o el numero_2
    # es mayor a -2
    # Imprima en pantalla si se cumple o no la condición
    if numero_1 < 10 or numero_2 > -2:
        print("Cumple la condicion de que el numero 1 sea menor a 10 o el segundo numero sea mayor a -2")
    else:
        print("No cumple con la condicion. El primer numero ingresado es mayor a 10 o el segundo numero es menor a -2")


def ej2():
    # Ejemplos variables de texto

    # Comparadores
    # Ingrese dos palabras cualesquiera y realice las sigueintes
    # comparaciones entre ellas
    texto_1 = str(input('Ingrese la primera palabra:\n'))

    texto_2 = str(input('Ingrese la segunda palabra:\n'))

    # Compare cual de las dos palabras es mayor (alfabéticamente)
    # Imprima en pantalla según corresponda
    if texto_1 > texto_2:
        print("El primer texto es mayor alfabeticamente")
    else:
        print("El segundo texto es mayor alfabeticamente")

    # Compare cual de las dos palabras tiene mayor
    # cantidad de letras
    # Imprima en pantalla según corresponda
    if (len(texto_1) > len(texto_2)):
        print("El primer texto ingresado tiene mayor cantidad de letras")
    else:
        print("El segundo texto ingresado tiene mayor cantidad de letras")

    # Verifique si la primera letra de la primera palabra
    # es mayor a la primera letra de la segunda palabra
    # Imprima en pantalla según corresponda
    if (texto_1[0] > texto_2[0]):
        print("El primer caracter del primer texto es mas grande que el primer caracter de el segundo texto")
    elif texto_1[0] == texto_2[0] :
        print("Los primeros caracteres son identicos")
    else:
        print("No cumple. El primer caracter de la primer palabra no es mayor que el primer caracter de la segunda palabra")

    copia_texto_1 = texto_1  # Copia de la variable texto_1

    # Verifique que copia_texto_1 es igual a texto_1
    # Imprima en pantalla según corresponda
    if copia_texto_1 == texto_1:
        print("copia texto 1 es igual a texto 1")
    else:
        print("No son iguales texto 1 y copia texto 1")

    # Verifique que copia_texto_1 es distinta a texto_2
    # Imprima en pantalla según corresponda
    if copia_texto_1 != texto_2:
        print("Copia texto 1 es diferente a texto 2")
    else:
        print("Copia texto 1 y texto 2 son iguales")

def ej3():
    # Ejercicios de práctica numérica

    # Condicionales anidados
    numero_1 = 4
    numero_2 = 4

    # Verifique si el numero_1 es mayor a 5
    #   --> En caso afirmativo, verifique si el numero_2
    #       es positivo
    #       --> En caso afirmativo imprima en pantalla "Resp=1"
    #       --> En caso negativo imprima en pantalla   "Resp=2"
    #  --> En caso negativo (numero_1 no es mayor a 5) 
    #      verifique si el numero_2 es mayor a 5
    #       --> En caso afirmativo imprima en pantalla "Resp=3"
    #       --> En caso negativo imprima en pantalla "Resp=4"

    if numero_1 > numero_2:
        if numero_2 > 0:
            print("Respt=1")
        else:
            print("Respt=2")
    elif numero_1 < 5:
        if numero_2 > 5:
            print("Respt=3")
        else:
            print("respt=4")

    # Verifique la calificación de un estudiante según su
    # puntaje en un examen
    puntaje = 40
    
    # Si el puntaje es mayor igual a 90 --> imprimir A
    # Si el puntaje es mayor igual a 80 --> imprimir B
    # Si el puntaje es mayor igual a 70 --> imprimir C
    # Si el puntaje es mayor igual a 60 --> imprimir D
    # Si el puntaje es manor a  60      --> imprimir F
    if puntaje >= 90:
        print("A")
    elif puntaje >=80 and puntaje < 90:
        print("B")
    elif puntaje >=70 and puntaje < 80:
        print("C")
    elif puntaje >= 60 and puntaje <= 70:
        print("D")
    else:
        print("F")
    # Debe imprimir en pantalla la calificacion
    # Utilizar "if" anidados




def ej4():
    # Ejemplos variables de texto

    texto_1 = '2'
    texto_2 = '2'

    # Verifique cual cual de los dos textos es mayor alfabéticamente
    # Imprima en pantalla según corresponda
    if texto_1 > texto_2:
        print("el texto 1 es mayor al texto 2")
    elif texto_1 == texto_2:
        print("los textos son iguales")
    else:
        print("El texto 2 es mayor al texto 1")

    # Transforma esas variables tipo texto y almacénalas
    # en nuevas variables númericas (int)
    numero_1 = int(texto_1) 
    numero_2 = int(texto_2)

    # Repita el proceso, ¿Cuál de las nuevas variables es mayor?
    # Imprima en pantalla según corresponda
    if  numero_1 > numero_2:
        print("El texto 1 es mayor")
    elif numero_1 == numero_2:
        print("Los textos son identicos")
    else:
        print("Texto 2 es mayor que texto 1")
    

    # Para pensar!
    # ¿Por qué cree que texto_2 es mayor a texto_1?
    # Siendo números tiene sentido, pero son caracteres, texto,
    # aún así el operador arroja el mismo resultado que con las
    # variables numéricas, cierto? ¿Por qué creen que es así?
    # Esta pregunta estará repetida en el Campus para que puedan
    # responder.
    # NOTA: La respuesta no se encuentra en el apunte, sino en Google ;)

if __name__ == '__main__':
    print("Bienvenidos a otra clase de Inove con Python")
    #ej1()
    #ej2()
    #ej3()
    ej4()

