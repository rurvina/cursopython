# -*- coding: utf-8 -*-
"""
Spyder Editor

Curso: Python Essentials
Fecha: 24/Nov/2021
Ejercicio: 01
Estudiante: Renato Urvina
"""
# impresión de título con cadena en 2 líneas 
# con caracteres de escape y tabulacion 
 
print("\n\tEmpezando a trabajar con Python \n"
"\tRealizado por: Renato Urvina\n")

print("\tConsultando los tipos de valores:\n")

# impresión con función anidada type para que el intérprete
# indique el tipo de dato  
print("\tEl tipo de dato de 875 es:\n\t ", type(875))
print("\n\tEl tipo de dato de 4.89 es:\n\t ", type(4.89))
print("\n\tEl tipo de dato de del texto: Now is better than never. es:\n\t",   
      type('Now is better than never.'))
print("\n\tEl tipo de dato de 1.32 es:\n\t ", type(1.32))

# salto de línea para la siguiente sección 
print("")

# impresión con función anidada isinstance para determinar si un valor es o no un tipo de dato
# En particular el valor 5 + 8i (número complejo) no se puede interpretar en esa forma
# y debe pasarse solo como cadena de caracteres
print("\n\t¿El valor 5 + 8i corresponde a un valor entero?\n\t", isinstance(('5+8i'), int))

print("\n\t¿El valor 8.2 corresponde a un valor entero?\n\t", isinstance((8.2), int))

# la función print admite que el texto y la función anidada puedan estar en 
# más de una línea
print("\n\t¿El texto: Readability counts. corresponde a un string?\n\t", 
      isinstance(('Readability counts.'), str))
