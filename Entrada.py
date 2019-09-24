#A entrada se le  almacenara valores
#type para declarar que tipo de dato es
entrada=input()
print(type(entrada))

#Los métodos isdigit () devuelven "True" si todos los caracteres de la cadena son dígitos
# si no todos son digitos de lo contrario, devuelve "False".
esEntero=(entrada.isdigit() and entrada.find(".")==-1)
if (esEntero):

#se ejecuta si la condicion es verdadera, entero
    print("Dato entero.¡Muy bien!")
else:

#si la condicion es falsa
    print("Dato no es entero. Intentar nuevamente.")