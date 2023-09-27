#Código de fundamentos de probabilidad y estadística
#Primer metodo: Utilizar el lado de un triángulo equilatero en python
import math

#definiendo variables
valor = float(input('Ingrese un valor para distribuirlo entre el triangulo: '))
valor = valor / 3

#Comprobando valores
if valor >= 0: 
    #Definiendo el area
    area = (valor ** 2) * (math.sqrt(3) / 4)
    print(f'El area de un triangulo equilatero es de {area}')
else:
    #En caso de que valor != 0: 
    print('proceso terminado')