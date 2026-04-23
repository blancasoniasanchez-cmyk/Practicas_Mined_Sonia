#Programa para evaluar si un estudiante aprueba, debe de recuperar o reprueba una asignatura
#Asignatura: Ciencia de la Computación
print("--------------------------------------------------------------------------------------")
#Inicio con un Mensaje de Bienvenida
print("Bienvenidos al Sistema de Evaluación de la Asignatura de Ciencias de la Computación")

#La función input()permite que el usuario ingrese datos desde la terminal
nombre =  input("Ingrese el nombre del estudiante:")

#La función input() permite que el usuario ingrese datos desde la terminal
#La funcón Float() permite que el usuario ingrese numeros enteros y decimales
nota = float(input("Ingrese la nota del estudiante: "))

#Condición de aprobación, si la nota es mayor o igual a 7
#Si se cumple se muestra en la terminal el mensaje de aprobado acompañado de un emoji 😃 con el nombre ingresado
if nota >=7:
    print("¡Felicidades! " + "\U0001F600 " +  nombre  + " haz aprobado la asignatura")

#Condición de recuperación, si la nota es mayor o igual a 5
#Si se cumple se muestra en la terminal el mensaje de reprobación acompañado de un emoji 😦 con el nombre ingresado
elif nota >=5:
    print("Lo sentimos" + "\U0001F627 " + nombre + " deberá de iniciar el proceso de recuperación de la asignatura ")

#Condición de recuperación, si la nota es menor a 5
#Si se cumple se muestra en la terminal el mensaje de reprobaceión acompañado de unemoji 😞 con el nombre ingresado
else:
    print("Desafortunadamente" + "\U0001F61E " + nombre + " haz reprobado  la asignatura")
print("-----------------------------------------------------------------------------------")
