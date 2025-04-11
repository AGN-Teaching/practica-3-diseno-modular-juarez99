"""
Funciones para calcular el índice de Fernandez Huerta (utilizando el módulo
analisis
_
texto) y para decidir el nivel de legibilidad de un texto.
"""
import analisis
_
texto as at # se llava a los módulos de el script
'analisis
_
texto' para poder crear el índice
def indice
_
FH(texto):
"""Calcula y devuelve el índice de Fernández Huerta del texto de
entrada.
"""
oraciones = at.contar
_
oraciones(texto)
palabras = at.contar
_palabras(texto)
silabas = at.contar
_
silabas(texto)
"""L = 206.84 - 1.02 (palabras / oraciones) - 60 (sílabas / palabras)"""
indice = 206.84 - 1.02 * (palabras / oraciones) - 60 * (silabas /
palabras)
return oraciones, palabras, silabas, indice
def nivel
_
legibilidad
_
FH(indice):
"""Decide y devuelve el nivel de legibilidad de un texto de acuerdo con
el índice de Fernández Huerta.
"""
if indice >= 90: # se utiliza una estructura de control selectiva para
evaluar el nivel de legibilidad
nivel = 'Muy fácil'
elif indice >= 80:
nivel = 'Fácil'
elif indice >= 70:
nivel = 'Relativamente fácil'
elif indice >= 60:
nivel = 'Normal'
elif indice >= 50:
nivel = 'Relativamente difícil'
elif indice >= 30:
nivel = 'Difícil'
else:
nivel = 'Muy difícil'
return nivel
