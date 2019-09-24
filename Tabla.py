#se  le pide al usuario un numero
numero=input("Dame un numero del 1 al 9: ")
#funcion int para convertir el valor a entero
numero=int(numero)

#for es un ciclo se ejecuta tantas veces como elementos tenga un  elemento
#elementos de una lista o de un range(), caracteres de una cadena
for i in range(1,11):
#la variable de control "i" puede otorgar otro nombre
    salida="{} x {} = {}"
    print(salida.format(numero,i,i*numero))