def contar
_
oraciones(texto):
# Se crea una lista de signos que marcan el fin de una oración.
signos
_
puntuacion = ['
.
'
,
'?'
,
'!'
,
';'
,
':']
# Crear un contador de oraciones.
contador
_
oraciones = 0
# el for revisara cada carácter del texto.
for caracter in texto:
if caracter in signos
_
puntuacion:
# cuando detecte un signo de puntiación se iran contando las
oraciones
contador
_
oraciones += 1
return contador
_
oraciones
def contar
_
palabras(texto):
# Dividir el texto en palabras utilizando split()
palabras = texto.split()
return len(palabras)
def contar
_
silabas(texto):
texto = texto.lower()
vocales = "aeiouáéíóú"
cantidad
_
silabas = 0
if texto[-1] in '
.,;:!?':
texto = texto[:-1]
if texto[-1] == 's':
texto = texto[:-1]
if texto[-2:] == 'es':
texto = texto[:-2]
# se dividen las palabras y se revisa una por una hasta encontrar una vocal e
irlas almacenando en el contador de silabas
for palabra in texto.split():
if palabra[0] in vocales:
cantidad
_
silabas += 1
for i in range(1, len(palabra)):
if palabra[i] in vocales and palabra[i - 1] not in vocales:
cantidad
_
silabas += 1
return cantidad
