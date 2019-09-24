for i in range(1,11):
    encabezado="Tabla del {}"
    print(encabezado.format(i))
#print sin argumentos es un salto de linea

    print()
#Dentro de un for, se pone otro for
    for j in range(1,11):
        #Aqui, i contiene el numero de base de la tabla
        #j el elemento de la tabla


        salida="{} x {} = {}"
        print(salida.format(i,j,i*j))
    else:
        #Se ejecuta este codigo que es un salto de linea

        print()