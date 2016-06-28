# TUPLAS : Varios datos inmutables
# Se Declara con parentesis ()

mi_tupla = ('textos', 15, 36, 36.58, 'otro string')
print(mi_tupla[0])
print(mi_tupla[0:3])


# LISTAS : igual a las tuplas, pero permite modificarlos y agregar nuevos 
# emplenado append() 
# Se Declara con corchetes []

mi_lista = ['textos', 15, 36, 36.58, 'otro string']
print(mi_lista[0])
mi_lista[0] = 'TEXTO NUEVO'
print(mi_lista[0])

mi_lista.append('56')
print(mi_lista)


# DICCIONARIOS : Se accede usando KEY no indice como las anteriores
# Se Declara con llaves {}

mi_diccionario = {
				'clave_1' : 52,
				'clave_2' : 36,
				'clave_3' : 3333
				  }

print(mi_diccionario['clave_1'])
print(mi_diccionario['clave_3'])



# TODO: operaciones con tuplas, listas y diccionarios