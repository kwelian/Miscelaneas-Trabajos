print("Miscelanea de Trabajo en Python\n")

print("Operadores\n")

print("Area de un triangulo\n")

base = float(input("Digite la base del triangulo:\n"))
altura = float(input("Digite la altura del triangulo:\n"))
area = base * altura / 2

print("El Area del triangulo es: ", str(area))

print("\n")

print("----------"*4)

print("Miscelanea de Trabajo\n")

print("Operadores\n")

print("Suma de dos Numeros\n")

num1 = float(input("Digite el primer numero:\n"))
num2 = float(input("Digite el segundo numero:\n"))
resultado = num1 + num2

print("La suma de los numeros es: ", str(resultado))

print("\n")

print("----------"*4)

print("Miscelanea de Trabajo\n")

print("Operadores\n")

print("Numero al cuadrado\n")

numero = int(input("Digite el numero\n"))

print("El resultado al cuadrado del numero", str(numero**2))

print("\n")

print("----------"*4)

print("Miscelanea de Trabajo\n")

print("Operadores\n")

print("Conversor de Unidades\n")

unidad = float(input("Digite la cantidad que desea convertir\n"))
print("Cantidad en dolar: " + str(unidad * 105.24))

print("\n")

print("----------"*4)

print("Miscelanea de Trabajo\n")

print("Operadores\n")

print("Perimetro y Area de un cuadrado\n")

print("\n")

print("----------"*4)

print("Perimetro del cuadrado\n")

perimetro = float(input("Digite el valor del perimetro:\n"))
print("El perimetro del cuadrado es:",
      str(perimetro + perimetro + perimetro + perimetro))

print("\n")

print("---"*4)

print("Area del cuadrado\n")

area = float(input("Digite el valor del area\n"))
print("El area  del cuadrado es:", area * area, "cm²")

print("\n")

print("----------"*4)

print("Miscelanea de Trabajo\n")

print("Operadores\n")

print("Area y Volumen de un cilindro\n")

print("Area de un cilindro\n")

radio = int(input("Digite el radio del cilindro\n"))
altura = int(input("Digite la altura del cilindro\n"))
area = str(2 * 3.14 * radio * altura + 2 * 3.14 * radio**2)

print("El area del cilindro es:", str(area))

print("\n")

print("---"*4)

print("Volumen del cilindro\n")

radio1 = int(input("Digite el radio del cilindro\n"))
altura1 = int(input("Digite la altura del cilindro\n"))

volumen = str(3.14 * radio1**2 * altura1)

print("El volumen del cilindro es", volumen, "cm3")

print("\n")

print("----------"*4)

print("Miscelanea de Trabajo\n")

print("Operadores\n")

print("Area y Longitud de una circunferencia\n")

parametro = float(input("Digite el parametro del circulo\n"))

print("El radio es", str(parametro / 3.14))

print("Digite el radio para calcular el area y la longitud\n")

radio = float(input("Digite el radio\n"))
area = 3.14 * radio**2
longitud = 2 * 3.14 * radio
print("El area del circulo es", str(area))
print("La longitud del circulo es", str(longitud))

print("\n")

print("----------"*4)

print("Miscelanea de Trabajo\n")

print("Operadores\n")

print("Promedio de 3 numeros\n")

numero1 = float(input("Digite el primer numero\n"))
numero2 = float(input("Digite el segundo numero\n"))
numero3 = float(input("Digite el tercer numero\n"))
promedio = numero1 + numero2 + numero3

print("El promedio de los numero es", str(promedio / 3))


print("\n")

print("----------"*9)


print("Miscelanea de Trabajo\n")

print("Condicionales\n")

print("Numero Positivo o Negativo\n")

numero = float(input("Digite el numero\n"))

if numero > 0:
    print("El numero es Positivo\n")

elif numero == 0:
    print("El numero es Cero")

else:
    print("El numero es Negativo\n")
print("\n")

print("----------"*4)
print("Miscelanea de Trabajo\n")

print("Condicionales\n")

print("Numero Mayor  o Menor\n")

numero = float(input("Digite el primer numero:\n"))

numeroDos = float(input("Digite el segundo numero\n"))

if numero > numeroDos:
    print("El numero:", numero, "Es mayor")

    print("Por lo tanto el numero:", numeroDos, "Es menor")


else:
    print("El numero:", numeroDos, "Es mayor")
    print("Por lo tanto el numero:", numero, "Es menor")

print("\n")

print("----------"*4)

print("Numeros Positivos Enteros Menor o Mayor\n")

numero = int(input("Digite el primer numero:\n"))

print("\n")

numeroDos = int(input("Digite el segundo numero:\n"))

print("\n")

numeroTres = int(input("Digite el tercer numero:\n"))

if numero < numeroDos < numeroTres:
    print("El numero:", numero, "Es menor que:",
          numeroDos, "Y que:", numeroTres)

elif numero > numeroDos < numeroTres:
    print("El numero:", numero, "Es mayor que:",
          numeroDos, "Y menor que:", numeroTres)

elif numero < numeroDos > numeroTres < numero:
    print("El numero:", numero, "Es menor que:",
          numeroDos, "Y mayor que:", numeroTres)


elif numero > numeroDos > numeroTres:
    print("El numero:", numero, "Es mayor que:",
          numeroDos, "Y que:", numeroTres)

elif numero > numeroDos < numeroTres:
    print("El numero:", numero, "Es mayor que:",
          numeroDos, "Y menor que:", numeroTres)

elif numero > numeroDos > numeroTres < numero:
    print("El numero:", numero, "Es menor que:",
          numeroDos, "Y mayor que:", numeroTres)

elif numero < numeroDos > numeroTres < numero:
    print("El numero:", numero, "Es menor que:",
          numeroDos, "Y mayor que:", numeroTres)

elif numero < numeroDos > numeroTres > numero:
    print("El numero:", numero, "Es menor que:",
          numeroDos, "Y menor que:", numeroTres)
  
print("\n")

print("----------"*4)

print("Miscelanea de Trabajo\n")

print("Condicionales\n")

print("A y B Suma o Resta\n")

A = float(input("Digite el primer numero (A)\n"))

B = float(input("Digite el segundo numero(B)\n"))

resultadoUno = A + B
resultadoDos = A - B

if A >= B:
    print("La suma es:", str(resultadoUno))

elif A < B:
    print("La resta es:", str(resultadoDos))

print("\n")

print("----------"*4)

print("Miscelanea de Trabajo\n")

print("Condicionales\n")

print("A y B Division\n")

A = float(input("Digite el primer numero (A)\n"))

B = float(input("Digite el segundo numero(B)\n"))

resultado = A / B

if (resultado > 0):
    print("La division es:", str(resultado))

else:
    print("La operacion no se puede ejecutar")

print("\n")

print("----------"*4)

print("Miscelanea de Trabajo\n")

print("Condicionales\n")

print("A y B Suma o Multiplicacion\n")

A = float(input("Digite el primer numero (A)\n"))

B = float(input("Digite el segundo numero(B)\n"))

resultadoUno = A + B
resultadoDos = A * B

if (A and B > 0):
    print("La suma es:", str(resultadoUno))


elif (A or B < 0):
    print("La multiplicacion es:", str(resultadoDos))

print("\n")

print("----------"*4)

print("Miscelanea de Trabajo\n")

print("Condicionales\n")

print("Año Bisiesto\n")


año = int(input("Escriba el año:\n"))


if (año % 4 == 0 and año % 100 != 0):
    print("Si es año bisiesto")

elif (año % 100 == 0 and año % 400 == 0):
    print("Si es año bisiesto")

else:
    print("No es año bisiesto")