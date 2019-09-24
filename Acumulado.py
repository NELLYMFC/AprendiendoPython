#Se declara dos variables uno de tipo entero y otro de tipo cadena
acumulado=int(0)
numero=str("")

#while es un ciclo  que no se rompe hasta  que se utilice la instruccion break
while True:
    numero=input("Dame un numero entero: ")
    if numero=="":
        #Se le pide un numero al usuario
        #si es un numero entra al ciclo, sino se imprime vacio y salida del programa
        print("Vacio. Salida del programa.")
        break
    else:
        # en la variable acumulado se almacenara los numeros que otorgara el usuario por cada cilo
        acumulado+=int(numero)
        salida="Monto acumulado: {}"
        print(salida.format(acumulado))
        #Montoacumulado:() + lo que se estuvo acumulando 