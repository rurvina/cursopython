# -*- coding: utf-8 -*-
"""
Created on Wed Nov 24 20:20:04 2021

Curso: Python Essentials
Fecha: 24/Nov/2021
Ejercicio: 01
Estudiante: Renato Urvina
"""


 
print("\n\tPrograma que identifica el tipo de dato de un valor "
      "ingresado por el usuario, se realizarán cinco interacciones: \n")

# Se asignará a una variable el valor ingresado por el usuario
# luego se imprimirá con la función anidada type

a = input("Primera Interacción, ingrese un valor cualquiera: ")
print("\nEste tipo de dato en Python es:\n", type(a) )

b = input("Segunda Interacción, ingrese un valor cualquiera: ")
print("\nEste tipo de dato en Python es:\n", type(b) )

c = input("Tercera Interacción, ingrese un valor cualquiera: ")
print("\nEste tipo de dato en Python es:\n", type(c) )

d = input("Cuarta Interacción, ingrese un valor cualquiera: ")
print("\nEste tipo de dato en Python es:\n", type(d) )

e = input("Quinta Interacción, ingrese un valor cualquiera: ")
print("\nEste tipo de dato en Python es:\n", type(e) )

print("\n Gracias por su colaboración \n ¡YA NO SE HARÁN MÁS INTERACCIONES!")
