
# Python posee muchas librerias(modulos) 
#import  se utiliza para hacer referencia a otros modulos
import random
#Se declara una variable de tipo float(decimal), y se asigna un valor
numero1=float(10.5)

#Para declarar una función  se debe poner la palabra "def" seguido del nombre de la función
#para el ejemplo le hemos puesto "mifuncion", en los paréntesis deben ir los parámetros
#ejemplos de parametros(5+10)
def  miFuncion():
#Se convierte a  tipo flotante
# Casi todas las funciones del módulo dependen de la función básica random () 
    numero2=float(random.randrange(1,10))

#Se utiliza mensaje para mostrar los resultados
    mensaje="La suma de {} y {} es {}"
    print(mensaje.format(numero1,numero2,numero1+numero2))

#Se declara la funcion definida en el codigo
    miFuncion()