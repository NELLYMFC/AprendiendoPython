#Se le pide al usuario dos numeros, por separado
numero1=input("Numero 1:")
numero2=input("Numero 2:")
salida= "Numeros proporcionados: {} y {}.{}."
# la salida= es lo que se va a imprimir junto con los numeros que brindo el usuario

# if se utiliza como condicion
if(numero1==numero2):
#Si los numeros capturados son iguales
    print(salida.format(numero1,numero2,"Los numeros son iguales"))
#Se imprime los numeros
else:
# else, entra cuando la primera condicion no se cumple 
    if numero1>numero2:
        #Reporta si el primer numero es mayor al segundo
        print(salida.format(numero1, numero2,"El mayo es el primero"))
    else:
# si no se cumplen las otras dos condiciones por logica entra la tercera 
        print(salida.format(numero1,numero2,"El mayor es el segundo"))