
#se captura un numero y se almacena pero antes se cambia a entero
numero=int(input("Dame un numero entero:"))

#se declaran tres variables donde se almacenaran los valores si el resultado es cero entra a la primera condicion
esMultiplicado3=((numero%3)==0)
esMultiplicado5=((numero%5)==0)
esMultiplicado7=((numero%7)==0)

# and  todas las condiciones son verdaderas
# or al menos una si es verdadera
#si  el valor es cero es correcto
if((esMultiplicado3 and esMultiplicado5) or esMultiplicado7):
    print("Correcto.")
else:
    print("Incorrecto.")
    # si, no  le aclarara al usuario que el valor es incorrecto