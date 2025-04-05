# Desafío 02 - Calcular el área de un rectángulo con presentación

# Define dos variables numéricas que representen el ancho y el largo de un rectángulo.
# Define variables de tipo string que contengan texto explicativo sobre lo que hace el programa.
# Calcula el área del rectángulo.
# Utiliza tanto variables numéricas como de texto para presentar el resultado de una manera que
# sea fácil de entender para alguien que no está viendo el código.

# Definición de variables numéricas
ancho = 6  # ancho del rectángulo
largo = 10  # largo del rectángulo

# Defición de variables string
titulo = "Programa para calcular el área de un rectángulo."
definicion = "El cálculo del área de un rectángulo es la multiplicación del ancho por el largo."

# Cálculo matemático
area = ancho * largo  # se define la variable area

# Presentación Gráfica
print()
print(titulo)
print()
print(definicion)
print()
print( "Presione ENTER para ver la representación" )
input()
print()
print("         LARGO           ")
print("├<─────────────────────>┤   ")
print("┌───────────────────────┐   ┬ ")
print("│                       │   │ A") 
print("│                       │   │ N")
print("│         ÁREA          │   │ C")
print("│                       │   │ H")
print("│                       │   │ O")
print("└───────────────────────┘   ┴ ")
print()
print("El ancho del rectángulo es: ", (ancho),)
print()
print("El largo del rectángulo es: ", (largo),)
print()
print("El área del rectángulo es: ", (area),)
print()
print()
print("Programa finalizado")
print()
input("Presione ENTER para cerrar")