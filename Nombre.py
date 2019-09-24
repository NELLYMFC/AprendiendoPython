#La funcion input se utiliza cuando queremos interactuar con el usuario
#se declara dos variables donde se le pide al usuario su nombre y su apellido

nombre=input("Nombre:")
apellidos=input("Apellidos:")
#se concatena los dos valores str que otorga el usuario
#declaramos otra variable donde se guardara el nombre y apellido para poder unirlos
#"" son para otorgar un espacio
nombreCompleto=nombre+" "+apellidos

#.upper es utilizado para representar las variables en mayusculas
nombreCompleto=nombreCompleto.upper()
print(nombreCompleto)