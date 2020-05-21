#!/usr/bin/env python
'''
Condicionales [Python]
Ejercicios de práctica
---------------------------
Autor: Inove Coding School
Version: 1.1
 
Descripcion:
Programa creado para que practiquen los conocimietos adquiridos durante la semana
'''

__author__ = "Inove Coding School"
__email__ = "alumnos@inove.com.ar"
__version__ = "1.1"

def ej1():
    # Ejercicios de práctica con números

    '''
    Realice un programa que solicite por consola 2 números
    Calcule la diferencia entre ellos e informe por pantalla
    si el resultado es positivo, negativo o cero.
        
    '''
    print("Ingrese el primer numero")
    numero_1 = int(input())
    print("Ingrese el segundo numero")
    numero_2 = int(input())

    resultado = numero_1 - numero_2

    if resultado > 0:
      print("La diferencia entre los numeros es positiva")
    elif resultado == 0:
      print("La diferencia entre los numeros es 0")
    else:
      print("La diferencia entre los numeros es negativa")


def ej2():
# Ejercicios de práctica con números

  '''
    Realice un programa que solicite el ingreso de tres números
    enteros, y luego en cada caso informe si el número es par
    o impar.
    Para cada caso imprimir el resultado en pantalla.
    
  '''
  print("Ingrese el primer entero")
  num_1 = int(input())
  print("Ingrese el segundo entero")
  num_2 = int(input())
  print("Ingrese el tercer entero")
  num_3 = int(input())

  if (num_1 % 2) == 0:
    print("El primer entero es par")
  else:
    print("El primer entero es impar")
  
  if(num_2 % 2) == 0:
    print("El segundo entero es par")
  else:
    print("El segundo entero es impar")
  
  if (num_3 % 2) == 0:
    print("El tercero entero es par")
  else:
    print("El tercero entero es impar")

def ej3():
    # Ejercicios de práctica con números

    '''
    Realice una calculadora, se ingresará por línea de comando dos números
    Luego se ingresará como tercera entrada al programa el símbolo de la operación
    que se desea ejecutar
    - Suma (+)
    - Resta (-)
    - Multiplicación (*)
    - División (/)
    - Exponente/Potencia (**)

    Se debe efectuar el cálculo correcto según la operación ingresada por consola
    Imprimir en pantalla la operación realizada y el resultado
    

    '''
    print("Ingrese el primer numero a calcular: ")
    num_1 = float(input(""))
    print("Ingrese el segundo numero a calcular")
    num_2 = float(input())

    print("Ingrese la operacion que desea realizar con el simbolo correspondiente:")
    print("-Suma ( + )");print("Resta ( - )");print("Multiplicacion ( * )");print("Division ( / )");print("Exponencial (**)")
    opcion = str(input())

    if opcion == "+":
      resultado = num_1 + num_2
      print("El resultado es: {}".format(resultado))

    elif opcion == "-":
      resultado = num_1 - num_2
      print("El resultado es: {}".format(resultado))

    elif opcion == "*":
      resultado = num_1 * num_2
      print("El resultado es: {}".format(resultado))
    
    elif opcion == "/":
      resultado = num_1 / num_2
      print("El resultado es: {}".format(resultado))

    elif opcion == "**":
      resultado = num_1 ** num_2
      print("El resultado es: {}".format(resultado))
    
    else:
      print("No esta indicando una operacion valida")


    
def ej4():
    # Ejercicios de práctica con cadenas
    
    '''
    Realice un programa que solicite por consola 3 palabras cualesquiera
    Luego el programa debe consultar al usuario como quiere ordenar las palabras
    1 - Ordenar por orden alfabético (usando el operador ">")
    2 - Ordenar por cantidad de letras (longitud de la palabra)

    Si se ingresa "1" por consola se deben ordenar las 3 palabras por orden alfabético
    e imprimir en pantalla de la mayor a la menor

    Si se ingresa "2" por consola se deben ordenar las 3 palabras por cantidad de letras
    e imprimir en pantalla de la mayor a la menor

  '''

def ej5():
    # Ejercicios de práctica con números
       
    '''
    Realice un programa que solicite ingresar tres valores de temperatura
    De las temperaturas ingresadas por consola determinar:
    1 - ¿Cuáles de ellas es la máxima temperatura ingresada?
    2 - ¿Cuáles de ellas es la mínima temperatura ingresada?
    3 - ¿Cuál es el promedio de las temperaturas ingresadas?

    En cada caso imprimir en pantalla el resultado  

    '''

if __name__ == '__main__':
    print("Ejercicios de práctica")
    #ej1()
    #ej2()
    #ej3()
    #ej4()
    #ej5()
