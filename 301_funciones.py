# Con 
def mi_funcion():
	print("Funcion Basica sin parametros")


mi_funcion()

# Con parametros
def p(p1, p2):
	print(p1)
	print(p2)

p("Hola", "Mundo")


# Con parametros por defecto
def otra_funcion(p1 = "Telefono", p2 = 5648961651):
	print(p1)
	print(p2)

otra_funcion("Movil", 416548964)
otra_funcion()
