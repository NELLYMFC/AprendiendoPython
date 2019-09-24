# Se declara una variable de tipo str que seran numeros("")por que es tipo cadena sin espacios
# Otro ejemplo puede ser a= 2
numero="1234"

#Se coloca type por que no se sabe que tipo de dato es (int,float,str,bool)
print(type(numero))
#La cadena de numeros se va a cambiar de tipo cadena a numero entero
numero=int(numero)
#para leer la variable  a su tipo de dato original
print(type(numero))
# Otra formato de salida es utilizando  str.format()
# ()las variables ,numero="1234"
salida="El numero utilizado es {}"
print(salida.format(numero))